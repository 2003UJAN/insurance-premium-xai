import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_dataset():
    # Project root: insurance-premium-xai/
    BASE_DIR = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )

    data_path = os.path.join(
        BASE_DIR,
        "data",
        "insurance_premium_dataset_50000_records.csv"
    )

    # Explicit safety check
    if not os.path.exists(data_path):
        st.error(f"Dataset not found at: {data_path}")
        st.stop()

    return pd.read_csv(data_path)


