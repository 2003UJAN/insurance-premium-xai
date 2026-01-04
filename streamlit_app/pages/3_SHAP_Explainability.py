import streamlit as st
import shap
import matplotlib.pyplot as plt

from utils.load_data import load_dataset
from utils.model_utils import load_model, preprocess

st.header("SHAP Explainability")

df = load_dataset()
model = load_model()

df_proc = preprocess(df.copy())
X = df_proc.drop(columns=["insurance_premium"])

idx = st.slider(
    "Select Record Index",
    0,
    len(X) - 1,
    10
)

prediction = model.predict(X.iloc[[idx]])[0]
st.subheader(f"Predicted Premium: ₹ {int(prediction)}")

explainer = shap.Explainer(model)
shap_values = explainer(X)

fig, ax = plt.subplots(figsize=(8, 6))
shap.plots.waterfall(shap_values[idx], show=False)
st.pyplot(fig)
plt.close(fig)
