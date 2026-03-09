import streamlit as st
import pickle
import pandas as pd

# Load saved files
similarity = pickle.load(open('similarity.pkl','rb'))
data = pickle.load(open('songs.pkl','rb'))

st.title("🎵 Song Recommendation System")

song_list = data['song_title'].values

selected_song = st.selectbox(
    "Select a Song",
    song_list
)

def recommend(song):
    
    index = data[data['song_title'] == song].index[0]
    distances = similarity[index]

    song_list = sorted(list(enumerate(distances)),
                       reverse=True,
                       key=lambda x: x[1])[1:6]

    recommended = []

    for i in song_list:
        recommended.append(data.iloc[i[0]].song_title)

    return recommended


if st.button("Recommend Songs"):

    recommendations = recommend(selected_song)

    for song in recommendations:
        st.write(song)