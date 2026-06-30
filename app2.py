import streamlit as st
from Model import recommend, movie_list

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>e
.block-container{padding-top:2rem;padding-bottom:2rem;}
.hero{
background:linear-gradient(135deg,#111827,#1f2937);
padding:28px;border-radius:18px;border:1px solid #333;text-align:center;
}
.hero h1{color:#ff4b4b;font-size:50px;margin-bottom:0;}
.hero p{font-size:18px;color:#d1d5db;}
.card{
background:#20242f;
padding:18px;
border-radius:14px;
border-left:6px solid #ff4b4b;
margin-bottom:15px;
box-shadow:0 2px 8px rgba(0,0,0,.2);
}
.footer{text-align:center;color:#9ca3af;padding-top:20px;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>🎬 Movie Recommendation System</h1>
<p>Discover your next favourite movie using <b>Content‑Based Filtering</b>,
<b>TF‑IDF Vectorization</b> and <b>Cosine Similarity</b>.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

c1,c2,c3=st.columns(3)
c1.metric("🎥 Movies", f"{len(movie_list):,}")
c2.metric("🤖 Algorithm","TF‑IDF")
c3.metric("⭐ Results","Top 10")

with st.sidebar:
    st.header("📌 Project Information")
    st.success("**Dataset**\n\nTMDB Movies Metadata")
    st.info("**Algorithm**\n\nContent‑Based Filtering")
    st.info("**Vectorizer**\n\nTF‑IDF")
    st.info("**Similarity**\n\nCosine Similarity")
    st.divider()
    st.markdown("### 👨‍💻 Developer")
    st.write("**Parth Chourasia**")
    st.caption("Python • Streamlit • Scikit‑Learn • NLP")

st.divider()

selected_movie = st.selectbox(
    "🔍 Search or Select a Movie",
    options=movie_list,
    index=None,
    placeholder="Search a movie..."
)

left,mid,right = st.columns([1,2,1])
with mid:
    clicked = st.button("🎬 Recommend Movies", use_container_width=True)

if clicked:
    if not selected_movie:
        st.warning("Please select a movie first.")
    else:
        with st.spinner("Finding similar movies..."):
            movies = recommend(selected_movie)

        st.divider()
        st.subheader("🍿 Recommended Movies")

        if not movies:
            st.error("No recommendations found.")
        else:
            cols = st.columns(2)
            for i,m in enumerate(movies):
                with cols[i%2]:
                    st.markdown(
                        f"""
<div class="card">
<h4>🎥 {m}</h4>
<p>Recommendation #{i+1}</p>
</div>
""",
                        unsafe_allow_html=True
                    )

st.divider()
st.markdown("""
<div class="footer">
Built with ❤️ using <b>Python</b>, <b>Streamlit</b> and <b>Scikit‑Learn</b><br>
© Parth Chourasia
</div>
""", unsafe_allow_html=True)
