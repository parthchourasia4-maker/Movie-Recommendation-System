# 🎬 Movie Recommendation System

> A modern **Content-Based Movie Recommendation System** built using **Python, Scikit-Learn, NLP, and Streamlit**. The application recommends movies similar to your favorite movie using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## 🚀 Live Demo

### 🌐 Try the App

**🔗 Live Application**  
https://movie-recommendation-system-3rpujzhyhmevqdtcqlj5cw.streamlit.app/

**💻 GitHub Repository**  
https://github.com/parthchourasia4-maker/Movie-Recommendation-System

---

# ✨ Features

- 🎬 Content-Based Movie Recommendation
- 🔍 Search and Select Movies
- 🤖 TF-IDF Vectorization
- 📊 Cosine Similarity Recommendation Engine
- ⚡ Interactive Streamlit Dashboard
- 🎨 Modern & Responsive User Interface
- 📱 Fully Deployed Web Application

---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Machine Learning | Scikit-Learn |
| NLP | TF-IDF Vectorizer |
| Data Processing | Pandas, NumPy |
| UI Framework | Streamlit |
| Dataset | TMDB Movies Metadata |

---

# ⚙️ How It Works

The recommendation system follows these steps:

1. Load the TMDB Movies Metadata dataset.
2. Clean and preprocess movie information.
3. Merge important textual features into a single **Tag** column.
4. Perform text preprocessing:
   - Lowercase conversion
   - Punctuation removal
   - Stopword removal
   - Lemmatization
5. Convert movie descriptions into numerical vectors using **TF-IDF**.
6. Compute **Cosine Similarity** between all movies.
7. Recommend the **Top 10 most similar movies**.

---

# 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app2.py
├── model.py
├── movie_recommendation.ipynb
├── movies_metadata.csv
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
    ├── 01) Home Dashboard.png
    ├── 02) sidebar.png
    ├── 03)Search System.png
    └── 04)Recommendations.png
```

---

# 📸 Application Screenshots

## 🏠 Home Dashboard

![Home Dashboard](screenshots/01%29%20Home%20Dashboard.png)

---

## 📋 Project Information Sidebar

![Sidebar](screenshots/02%29%20sidebar.png)

---

## 🔍 Movie Search System

![Search System](screenshots/03%29Search%20System.png)

---

## 🎥 Movie Recommendations

![Recommendations](screenshots/04%29Recommendations.png)

---

# 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/parthchourasia4-maker/Movie-Recommendation-System.git
```

### Navigate to the Project Folder

```bash
cd Movie-Recommendation-System
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

# 🎯 Example

### Input

```text
Avatar
```

### Output

```text
Avatar 2
Avatar: Creating the World of Pandora
The Inhabited Island
Stand by Me Doraemon
Pandora and the Flying Dutchman
A Trip to the Moon
The War of the Robots
...
```

---

# 🚀 Future Improvements

- 🎬 Movie Posters
- ⭐ IMDb Ratings
- 📅 Release Date
- 📝 Movie Overview
- 🎭 Genre Filtering
- ❤️ Favorite Movies
- 🔥 Trending Movies
- 🌐 TMDB API Integration

---

# 👨‍💻 Author

**Parth Chourasia**

- 💼 LinkedIn: https://www.linkedin.com/in/parth-chourasia/
- 💻 GitHub: https://github.com/parthchourasia4-maker

---

# ⭐ Show Your Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

It helps support the project and motivates further development.

---

## Thank You for Visiting! 🎬🍿