import streamlit as st

st.set_page_config(
    page_title="Explainable Insurance Premium System",
    layout="wide"
)

st.title("Explainable AI for Insurance Premium Prediction")

st.markdown("""
This application demonstrates:
- 📊 Exploratory Data Analysis  
- 🗺️ City-wise premium heatmaps (OpenStreetMap)  
- 🧠 Explainable AI using SHAP  
""")

st.sidebar.success("Select a page from the sidebar")

