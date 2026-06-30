import streamlit as st

from Model import recommend, movie_list

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main{
    padding-top:2rem;
}

.title{
    font-size:42px;
    font-weight:bold;
    color:#ff4b4b;
}

.subtitle{
    font-size:18px;
    color:gray;
}

.movie-card{
    background-color:#262730;
    padding:15px;
    border-radius:10px;
    margin-bottom:12px;
    font-size:18px;
}

.footer{
    text-align:center;
    color:gray;
    font-size:14px;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Header
# ---------------------------------------------------

st.markdown(
"""
<div class='title'>
🎬 Movie Recommendation System
</div>

<div class='subtitle'>
Discover movies similar to your favourites using
<b>Content-Based Filtering</b>,
<b>TF-IDF Vectorization</b> and
<b>Cosine Similarity</b>.
</div>
""",
unsafe_allow_html=True
)

st.divider()

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

with st.sidebar:

    st.header("📌 Project Information")

    st.write("**Dataset**")
    st.success("TMDB Movies Metadata")

    st.write("**Algorithm**")
    st.info("Content-Based Filtering")

    st.write("**Vectorizer**")
    st.info("TF-IDF")

    st.write("**Similarity Measure**")
    st.info("Cosine Similarity")

    st.divider()

    st.write("### Developed By")

    st.write("Parth Chourasia")

# ---------------------------------------------------
# Movie Selection
# ---------------------------------------------------

selected_movie = st.selectbox(
    "🎥 Select a Movie",
    movie_list,
    index=0
)

col1, col2 = st.columns([1,4])

with col1:

    recommend_btn = st.button(
        "Recommend",
        use_container_width=True
    )

# ---------------------------------------------------
# Recommendation Output
# ---------------------------------------------------

if recommend_btn:

    with st.spinner("Finding similar movies..."):

        recommendations = recommend(selected_movie)

    st.divider()

    st.subheader("🍿 Recommended Movies")

    if len(recommendations)==0:

        st.error("Movie not found.")

    else:

        for i,movie in enumerate(recommendations,1):

            st.markdown(
                f"""
                <div class='movie-card'>
                <b>{i}.</b> {movie}
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.divider()

st.markdown(
"""
<div class='footer'>
Made with ❤️ using Python, Streamlit and Scikit-Learn
</div>
""",
unsafe_allow_html=True
)