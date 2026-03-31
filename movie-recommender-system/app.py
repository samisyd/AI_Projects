import pickle
import streamlit as st
import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TMDB_API_KEY")
if not api_key:
    st.error("TMDB API key not found. Check your .env file.")

session = requests.Session()


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": api_key,
        "language": "en-US"
    }
    
    response = session.get(url, params=params)
    
    if response.status_code != 200:
        return None
    
    data = response.json()
    poster_path = data.get("poster_path")
    
    return f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else None

def recommend(movie):

    if movie not in movies['title'].values:
        return [], []
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


import pickle
import os

BASE_DIR = os.path.dirname(__file__)

with open(os.path.join(BASE_DIR, 'model/movie_dict.pkl'), 'rb') as f:
    movies_dict = pickle.load(f)
    movies = pd.DataFrame(movies_dict)

with open(os.path.join(BASE_DIR, 'model/similarity.pkl'), 'rb') as f:
    similarity = pickle.load(f)

st.header('Movie Recommender System')

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    with st.spinner('Fetching recommendations...'):
        names, posters = recommend(selected_movie)
    
    st.subheader("Recommended Movies 🎬")
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(names[i])
            poster = posters[i] or "https://via.placeholder.com/500x750?text=No+Image"
            st.image(poster)







