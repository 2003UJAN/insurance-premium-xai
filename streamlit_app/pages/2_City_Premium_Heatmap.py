import streamlit as st
from streamlit_folium import st_folium
from utils.load_data import load_dataset
from utils.map_utils import create_city_map

df = load_dataset()

st.header("City-wise Insurance Premium Heatmap")

city = st.selectbox("Select City", df["city_name"].unique())
locality_type = st.selectbox(
    "Select Locality Type",
    df["locality_type"].unique()
)

filtered = df[
    (df["city_name"] == city) &
    (df["locality_type"] == locality_type)
]

if filtered.empty:
    st.warning("No data available.")
else:
    m = create_city_map(filtered)
    st_folium(m, width=800, height=500)

