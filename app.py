# command to run : streamlit run app.py

import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=711555776bd21301165afec356e76ee7&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def Recommend(movie):
    movie_idx = movies_list[movies_list['title'] == movie].index[0]
    distance_similarity = similarity_matrix[movie_idx]
    # we use enumerate function, so that our indexes not get corrupt while sorting.
    # then we sort the data and fetch top 5 similar movies.
    recommend_movies_list = sorted(list(enumerate(distance_similarity)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_poster = []
    for i in recommend_movies_list:
        movie_id = movies_list.iloc[i[0]].movie_id
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_poster


movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity_matrix = pickle.load(open('similarity_matrix.pkl', 'rb'))

movies = movies_list['title'].values

st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    'Select any movie to get recommended movies.',
    movies)

if st.button('Recommend'):
    movie_name, poster = Recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write(movie_name[0])
        st.image(poster[0])

    with col2:
        st.write(movie_name[1])
        st.image(poster[1])

    with col3:
        st.write(movie_name[2])
        st.image(poster[2])

    with col4:
        st.write(movie_name[3])
        st.image(poster[3])

    with col5:
        st.write(movie_name[4])
        st.image(poster[4])
