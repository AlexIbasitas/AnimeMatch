import streamlit
import pickle
import requests
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from fuzzywuzzy import fuzz

# pip: fuzzywuzzy, streamlit, pickle

animes = pickle.load(open("animes_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
THRESHOLD = 50


animes_list=animes['title'].values
animes_list = np.unique(animes_list)

bg_image = """
<style>
    [data-testid="stAppViewContainer"] {
        background-image: url('https://w.forfun.com/fetch/5d/5da2ee70680cb19f502b948091542132.jpeg');
        background-size: cover;
        color: black;
    }
</style>
"""

streamlit.markdown(bg_image, unsafe_allow_html=True)
streamlit.title("AnimeMatch")

searchbox = streamlit.selectbox("Explore new anime gems based on ones you already love!", animes_list)

def recommend(anime):
    index=animes[animes['title']==anime].index[0]
    original_title = anime
    scores = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    anime_titles = []
    anime_posters = []
    img_urls = []

    for s in scores:
        animes_id=animes.iloc[s[0]].uid
        similarity_score = fuzz.token_sort_ratio(animes.iloc[s[0]].title, original_title)
        if animes.iloc[s[0]].title in anime_titles or animes.iloc[s[0]].title == original_title or similarity_score > THRESHOLD:
            continue
        anime_titles.append(animes.iloc[s[0]].title)
        anime_posters.append(animes.iloc[s[0]].img_url)
        img_urls.append(animes.iloc[s[0]].link)
        if len(anime_titles) >= 5:
            break
    return anime_titles, anime_posters, img_urls



if streamlit.button("Generate"):
    anime_titles, anime_posters, img_urls = recommend(searchbox)
    rec1, rec2, rec3, rec4, rec5 = streamlit.columns(5, gap="small")
    with rec1:
        streamlit.text(anime_titles[0])
        streamlit.markdown(f'<a href="{img_urls[0]}" target="_blank"><img src="{anime_posters[0]}" style="max-width:100%; height:auto;" alt="Image"></a>', unsafe_allow_html=True)
    with rec2:
        streamlit.text(anime_titles[1])
        streamlit.markdown(f'<a href="{img_urls[1]}" target="_blank"><img src="{anime_posters[1]}" style="max-width:100%; height:auto;" alt="Image"></a>', unsafe_allow_html=True)

    with rec3:
        streamlit.text(anime_titles[2])
        streamlit.markdown(f'<a href="{img_urls[2]}" target="_blank"><img src="{anime_posters[2]}" style="max-width:100%; height:auto;" alt="Image"></a>', unsafe_allow_html=True)

    with rec4:
        streamlit.text(anime_titles[3])
        streamlit.markdown(f'<a href="{img_urls[3]}" target="_blank"><img src="{anime_posters[3]}" style="max-width:100%; height:auto;" alt="Image"></a>', unsafe_allow_html=True)

    with rec5:
        streamlit.text(anime_titles[4])
        streamlit.markdown(f'<a href="{img_urls[4]}" target="_blank"><img src="{anime_posters[4]}" style="max-width:100%; height:auto;" alt="Image"></a>', unsafe_allow_html=True)

