import pandas as pd
import plotly.express as px

import streamlit as st

st.title(" House Rocket Company")

st.markdown(" ## Welcome to House Rocket Data Analyais")

st.header("Load Data")

path = r'C:\Users\henry\repositorios_ds\Curso_python_ds\dataset\kc_house_data.csv'

@st.cache( allow_output_mutation= True )

def get_data(path):
    data = pd.read_csv(path)
    data['date'] = pd.to_datetime(data['date'])
    return data

df = get_data(path)

st.dataframe(df.head())

# bedrooms = st.sidebar.multiselect(
# "Número de quartos",
# df['bedrooms'].unique()
# )
#
# st.write(f"Sua escolha: {bedrooms[0]}")

st.header("House Rocket Map")

is_check = st.checkbox("Display map")



price_min = int(df['price'].min())
price_max = int(df['price'].max())
price_mean = int(df['price'].mean())

price_slider = st.slider("Price Range",
                         price_min,
                         price_max,
                         price_mean)
houses = df[df['price'] < price_slider][['id', 'lat', 'long', 'price']]


if is_check:

    fig = px.scatter_mapbox(houses,
                            lat='lat',
                            lon='long',
                            color_continuous_scale=px.colors.cyclical.IceFire,
                            size_max=5,
                            zoom=10

                            )

    fig.update_layout(mapbox_style='open-street-map')
    fig.update_layout(height=600, margin={'r': 0, 'l': 0, 't': 0, 'b': 0})
    st.plotly_chart(fig)
