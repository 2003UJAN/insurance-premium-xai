import joblib
import os
from sklearn.preprocessing import LabelEncoder

def load_model():
    BASE_DIR = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )

    model_path = os.path.join(
        BASE_DIR,
        "models",
        "premium_model.pkl"
    )

    return joblib.load(model_path)

def preprocess(df):
    df = df.drop(columns=["locality_name"])

    categorical_cols = [
        "city_name",
        "locality_type",
        "terrain_type",
        "natural_disaster_risk",
        "urban_flood_risk",
        "gender",
        "occupation_risk_level",
        "alcohol_consumption",
        "physical_activity_level",
        "health_checkup_frequency"
    ]

    for col in categorical_cols:
        df[col] = LabelEncoder().fit_transform(df[col])

    return df
