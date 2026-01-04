import streamlit as st
from streamlit_folium import st_folium

from utils.load_data import load_dataset
from utils.map_utils import create_hotspot_map

st.header("City-wise Insurance Premium Hotspots")

df = load_dataset()

city = st.selectbox(
    "Select City",
    sorted(df["city_name"].unique())
)

locality_type = st.multiselect(
    "Filter by Locality Type (optional)",
    sorted(df["locality_type"].unique()),
    default=list(df["locality_type"].unique())
)

filtered = df[
    (df["city_name"] == city) &
    (df["locality_type"].isin(locality_type))
]

if filtered.empty:
    st.warning("No data available for selected filters.")
else:
    st.markdown("""
    **Interpretation**
    - 🟢 Low premium hotspot  
    - 🟠 Medium premium hotspot  
    - 🔴 High premium hotspot  
    - Circle size indicates premium intensity
    """)

    m = create_hotspot_map(filtered)
    st_folium(m, width=900, height=550)
