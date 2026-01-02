import streamlit as st
import pickle
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# --- Robust session with retries ---
session = requests.Session()
session.mount(
    "https://",
    HTTPAdapter(
        max_retries=Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504],
        )
    ),
)

API_KEY = "8bd6f546cf8080173659ab9d321151cd"

def fetchposter(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        resp = session.get(
            url,
            params={"api_key": API_KEY, "language": "en-US"},
            timeout=8,
        )
        resp.raise_for_status()
        poster = resp.json().get("poster_path")
        return f"https://image.tmdb.org/t/p/w500/{poster}" if poster else None
    except Exception as e:
        print("Poster fetch failed:", e)
        return None


def recommend(selected_movie):
    movie_index = movies[movies['title'] == selected_movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    names, posters = [], []
    for i in movies_list:
        row = movies.iloc[i[0]]
        names.append(row.title)
        posters.append(fetchposter(row.movie_id))

    return names, posters


# --- Load data ---
similarity = pickle.load(open("similarity.pkl", "rb"))
movies = pd.DataFrame(pickle.load(open("movies_dict.pkl","rb")))

st.title("Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a movie",
    movies["title"].values
)

if st.button("Get recommendations"):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for col, name, poster in zip(cols, names, posters):
        with col:
            if poster:
                st.image(poster, caption=name, use_container_width=True)
            else:
                st.write(f"**{name}**")
                st.write("Poster unavailable")