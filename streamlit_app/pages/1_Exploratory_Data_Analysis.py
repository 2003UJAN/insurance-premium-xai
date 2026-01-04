import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

from utils.load_data import load_dataset

st.header("Exploratory Data Analysis")

df = load_dataset()

city = st.selectbox("Select City", df["city_name"].unique())
city_df = df[df["city_name"] == city]

st.subheader("Insurance Premium Distribution")
fig, ax = plt.subplots()
sns.histplot(city_df["insurance_premium"], bins=40, kde=True, ax=ax)
st.pyplot(fig)

st.subheader("Premium by Locality Type")
fig, ax = plt.subplots()
sns.boxplot(
    x="locality_type",
    y="insurance_premium",
    data=city_df,
    ax=ax
)
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("AQI vs Premium")
fig, ax = plt.subplots()
sns.scatterplot(
    x="avg_aqi",
    y="insurance_premium",
    data=city_df,
    alpha=0.4,
    ax=ax
)
st.pyplot(fig)
