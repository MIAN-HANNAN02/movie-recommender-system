import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=9f286f46907d438e0b11e7f558f9756e&language=en-US"
    data = requests.get(url).json()

    if 'poster_path' in data and data['poster_path'] is not None:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]]['id']
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]]['title'])

    return recommended_movies,recommended_movies_posters
with open('movies.pkl', 'rb') as f:
    movies_dict = pickle.load(f)
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie= st.selectbox(
    'Select a Movie'
    ,movies['title'])


if st.button('Show Recommendation'):
    recommended_movies, recommended_movies_posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_movies_posters[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_movies_posters[1])

    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_movies_posters[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_movies_posters[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_movies_posters[4])

