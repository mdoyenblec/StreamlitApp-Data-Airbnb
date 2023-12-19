import os 
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import time




def load_data(uploaded_file):
    data = pd.read_csv(uploaded_file)
    return data

def main():
    global geo

    st.title("Airbnb Paris Data Analysis September 2023")
    st.sidebar.success("Select a page above 👋🏼 !")

    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    data = load_data(uploaded_file)

    with st.spinner(text='In progress...'):
        time.sleep(3)

    st.subheader("Raw Data")
    st.write(data)


    ### PLOT 1 : Listings par arrondissement ###
    st.subheader("Number of Listings per Neighbourhood")
    grouped_data = data[["id", "neighbourhood_cleansed"]].groupby("neighbourhood_cleansed").count().sort_values(by="id", ascending=False)

    bar_chart = alt.Chart(grouped_data.reset_index()).mark_bar().encode(
            y=alt.Y('neighbourhood_cleansed:N', title='Neighbourhood', sort='-x'),
            x=alt.X('id:Q', title='Number of Listings')
        ).properties(
            width=900,
            height=700
        )
    st.altair_chart(bar_chart, use_container_width=True)
        
        
    ### PLOT 2 : Listings par accommodates ###
    st.subheader("Number of Listings per Accommodates 🧑🏻‍🦰👨🏼‍🦰")
    grouped_data_2 = data.groupby("accommodates").count().loc[:,"id"]

    bar_chart_2 = alt.Chart(grouped_data_2.reset_index()).mark_bar().encode(
            x=alt.X('accommodates:N', title='Accommodates'),
            y=alt.Y('id:Q', title='Number of listings')
            
        ).properties(
            width=900,
            height=700
        )
    st.altair_chart(bar_chart_2, use_container_width=True)



    ### GEOMAP JSON : Listings ###
    st.subheader("Visual Representation Listings ")
    st.map(data)

    # LINK JUPYTER NOTEBOOK
    st.subheader("Lien suite de l'analyse (Jupyter Notebook)") 
    jupyter_notebook_url = 'https://nbviewer.org/github/mdoyenblec/Airbnb-Paris-Analysis-Notebook/blob/main/notebook.ipynb'
    link_markdown = f'[Click here to open notebook]({jupyter_notebook_url})'
    st.markdown(link_markdown, unsafe_allow_html=True)


if __name__ == "__main__":
    main()



        
