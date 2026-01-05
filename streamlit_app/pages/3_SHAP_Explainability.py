import streamlit as st
import shap
import matplotlib.pyplot as plt
import pandas as pd

from utils.load_data import load_dataset
from utils.model_utils import load_model, preprocess

st.header("SHAP Explainability")

# -------------------------------------------------
# Load data and model
# -------------------------------------------------
df = load_dataset()
model = load_model()

# Preprocess for model input
df_proc = preprocess(df.copy())
X = df_proc.drop(columns=["insurance_premium"])

# -------------------------------------------------
# Record selector
# -------------------------------------------------
idx = st.slider(
    "Select Record Index",
    min_value=0,
    max_value=len(df) - 1,
    value=10
)

# -------------------------------------------------
# Show selected record details (WITHOUT last column)
# -------------------------------------------------
st.subheader("Selected Record Details")

# Drop target column ONLY for display
record_raw = df.iloc[idx].drop("insurance_premium")

record_df = pd.DataFrame(record_raw).reset_index()
record_df.columns = ["Feature", "Value"]

st.dataframe(record_df, use_container_width=True)

# -------------------------------------------------
# Prediction
# -------------------------------------------------
prediction = model.predict(X.iloc[[idx]])[0]
st.subheader(f"Predicted Premium: ₹ {int(prediction)}")

# -------------------------------------------------
# SHAP Explainability
# -------------------------------------------------
st.subheader("Why this premium? (SHAP Explanation)")

explainer = shap.Explainer(model)
shap_values = explainer(X)

fig, ax = plt.subplots(figsize=(8, 6))
shap.plots.waterfall(shap_values[idx], show=False)
st.pyplot(fig)
plt.close(fig)
