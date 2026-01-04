import folium
import numpy as np

def premium_color(premium, p_min, p_max):
    """Map premium to color"""
    if premium <= p_min + 0.33 * (p_max - p_min):
        return "green"
    elif premium <= p_min + 0.66 * (p_max - p_min):
        return "orange"
    else:
        return "red"

def create_hotspot_map(city_df):
    center_lat = city_df["latitude"].mean()
    center_lon = city_df["longitude"].mean()

    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=11,
        tiles="OpenStreetMap"
    )

    p_min = city_df["insurance_premium"].min()
    p_max = city_df["insurance_premium"].max()

    for _, row in city_df.iterrows():
        color = premium_color(
            row["insurance_premium"],
            p_min,
            p_max
        )

        folium.Circle(
            location=[row["latitude"], row["longitude"]],
            radius=200 + (row["insurance_premium"] / p_max) * 800,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.6,
            popup=f"""
            <b>{row['locality_name']}</b><br>
            Premium: ₹{int(row['insurance_premium'])}<br>
            AQI: {row['avg_aqi']}<br>
            Flood Risk: {row['urban_flood_risk']}
            """
        ).add_to(m)

    return m
