import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Airbnb Londres Analyse de marché V2')
st.title('Hello')

DATA_URL = ('http://data.insideairbnb.com/united-kingdom/england/london/2023-09-06/visualisations/listings.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data_load_state = st.text('Chargement des données...')
data = load_data(10000)
data_load_state.text("Fait! (using st.cache)")

if st.checkbox('Afficher les données raw'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Prix Moyen à Londres')
average_price_londres = data['price'].mean()
st.write(f"Le prix moyen à Londres est de {average_price_londres:.2f} €")

st.subheader('Prix Moyen par Quartier (Interactif)')
average_price_per_neighborhood = data.groupby('neighbourhood')['price'].mean().reset_index()
average_price_per_neighborhood_sorted = average_price_per_neighborhood.sort_values(by='price', ascending=False)
fig = px.bar(average_price_per_neighborhood_sorted, x='neighbourhood', y='price', 
             labels={'price': 'Prix Moyen', 'neighbourhood': 'Quartier'},
             title="Prix Moyen par Quartier à Londres")
st.plotly_chart(fig)

st.subheader('Nombre de Biens par Quartier')
count_per_neighbourhood = data['neighbourhood'].value_counts()
st.bar_chart(count_per_neighbourhood)

st.subheader('Carte Dynamique avec Prix des Logements')
st.map(data)

st.subheader('Nombre de Logements par Propriétaire')
properties_per_owner = data['host_name'].value_counts().head(10)  
st.bar_chart(properties_per_owner)



        
