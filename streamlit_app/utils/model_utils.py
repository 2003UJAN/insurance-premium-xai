import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_model():
    return joblib.load("/models/premium_model.pkl")

def preprocess(df):
    df = df.drop(columns=["locality_name"])

    categorical_cols = [
        "city_name","locality_type","terrain_type",
        "natural_disaster_risk","urban_flood_risk",
        "gender","occupation_risk_level",
        "alcohol_consumption","physical_activity_level",
        "health_checkup_frequency"
    ]

    for col in categorical_cols:
        df[col] = LabelEncoder().fit_transform(df[col])

    return df

