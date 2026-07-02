import warnings
import ast
import re

import pandas as pd
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

warnings.filterwarnings("ignore")



# -----------------------------------------------------
# Download NLTK Resources
# -----------------------------------------------------

nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


# -----------------------------------------------------
# Helper Functions
# -----------------------------------------------------

def convert_genres(text):
    """
    Convert genre list stored as string into plain text.
    """

    try:
        genres = ast.literal_eval(text)
        return " ".join([genre["name"] for genre in genres])
    except:
        return ""


def preprocess_text(text):
    """
    Clean and preprocess text.
    """

    text = str(text).lower()

    text = re.sub(r"[^a-zA-Z\s]", "", text)

    words = text.split()

    words = [
        word
        for word in words
        if word not in stop_words
    ]

    words = [
        lemmatizer.lemmatize(word)
        for word in words
    ]

    return " ".join(words)


# -----------------------------------------------------
# Load Dataset
# -----------------------------------------------------
from functools import lru_cache
@lru_cache(maxsize=1)
def load_dataset():

    df = pd.read_csv("movies_metadata.csv")

    df = df.drop_duplicates()

    df = df[
        [
            "title",
            "genres",
            "overview",
            "tagline",
            "popularity",
            "vote_average",
        ]
    ].copy()

    df.dropna(subset=["title"], inplace=True)

    df["overview"] = df["overview"].fillna("")
    df["tagline"] = df["tagline"].fillna("")
    df["popularity"] = df["popularity"].fillna("")
    df["vote_average"] = df["vote_average"].fillna("")

    df["genres"] = df["genres"].apply(convert_genres)

    df["tag"] = (
        df["title"]
        + " "
        + df["genres"]
        + " "
        + df["tagline"]
        + " "
        + df["overview"]
    )

    df["tag"] = df["tag"].apply(preprocess_text)

    df.reset_index(drop=True, inplace=True)

    return df


# -----------------------------------------------------
# Build Recommendation Model
# -----------------------------------------------------

df = load_dataset()

indices = (
    df.reset_index()
      .drop_duplicates(subset="title")
      .set_index("title")["index"]
)

tfidf = TfidfVectorizer(
    max_features=50000,
    ngram_range=(1, 2),
    stop_words="english",
)

tfidf_matrix = tfidf.fit_transform(df["tag"])


# -----------------------------------------------------
# Recommendation Function
# -----------------------------------------------------

def recommend(movie_name, n=10):

    if movie_name not in indices:
        return []

    movie_index = indices[movie_name]

    similarity_scores = cosine_similarity(
        tfidf_matrix[movie_index],
        tfidf_matrix
    ).flatten()

    similar_indices = similarity_scores.argsort()[::-1]

    recommendations = []
    seen = set()

    for idx in similar_indices:

        if idx == movie_index:
            continue

        if idx >= len(df):
            continue

        movie = df.iloc[idx]["title"]

        if movie in seen:
            continue

        seen.add(movie)
        recommendations.append(movie)

        if len(recommendations) == n:
            break

    return recommendations
# -----------------------------------------------------
# Available Movies
# -----------------------------------------------------

movie_list = sorted(df["title"].unique())