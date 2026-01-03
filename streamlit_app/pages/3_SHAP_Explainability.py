import streamlit as st
import shap
import matplotlib.pyplot as plt
from utils.load_data import load_dataset
from utils.model_utils import load_model, preprocess

shap.initjs()

df = load_dataset()
model = load_model()

st.header("Explainable AI (SHAP)")

# Sample selection
idx = st.slider("Select Record Index", 0, len(df)-1, 10)

df_proc = preprocess(df.copy())
X = df_proc.drop(columns=["insurance_premium"])

explainer = shap.Explainer(model)
shap_values = explainer(X)

st.subheader("Predicted Premium")
st.write(f"₹ {int(model.predict(X.iloc[[idx]])[0])}")

st.subheader("SHAP Waterfall Plot")
fig = plt.figure()
shap.plots.waterfall(shap_values[idx], show=False)
st.pyplot(fig)

