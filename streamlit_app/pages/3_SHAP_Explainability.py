import streamlit as st
import shap
import matplotlib.pyplot as plt

from utils.load_data import load_dataset
from utils.model_utils import load_model, preprocess

st.header("Explainable AI (SHAP)")

# Load data & model
df = load_dataset()
model = load_model()

# Preprocess
df_proc = preprocess(df.copy())
X = df_proc.drop(columns=["insurance_premium"])

# Select record
idx = st.slider(
    "Select Record Index",
    min_value=0,
    max_value=len(X) - 1,
    value=10
)

# Predict
prediction = model.predict(X.iloc[[idx]])[0]
st.subheader(f"Predicted Premium: ₹ {int(prediction)}")

# Create SHAP explainer
explainer = shap.Explainer(model)
shap_values = explainer(X)

# --- SHAP Waterfall Plot (Matplotlib-based, Streamlit-safe) ---
st.subheader("SHAP Explanation")

fig, ax = plt.subplots(figsize=(8, 6))
shap.plots.waterfall(shap_values[idx], show=False)
st.pyplot(fig)
plt.close(fig)
