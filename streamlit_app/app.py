import streamlit as st

st.set_page_config(
    page_title="Explainable Insurance Premium System",
    layout="wide"
)

st.title("Explainable AI for Insurance Premium Prediction")
st.markdown("""
This application demonstrates:
- Exploratory Data Analysis  
- City-wise premium heatmaps using OpenStreetMap  
- Explainable AI (SHAP) for premium transparency  
""")

st.sidebar.success("Select a page from above 👆")

