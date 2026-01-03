import pandas as pd
import streamlit as st

@st.cache_data
def load_dataset():
    return pd.read_csv("/data/insurance_premium_dataset_50000_records.csv")

