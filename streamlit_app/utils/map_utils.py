import folium

# -------------------------------
# Helper: premium → color bucket
# -------------------------------

def premium_color(premium, p_min, p_max):
    if premium <= p_min + 0.33 * (p_max - p_min):
        return "green"     # Low premium
    elif premium <= p_min + 0.66 * (p_max - p_min):
        return "orange"    # Medium premium
    else:
        return "red"       # High premium


# -------------------------------
# Main hotspot map function
# -------------------------------

def create_hotspot_map(city_df):
    # Center map on city mean location
    center_lat = city_df["latitude"].mean()
    center_lon = city_df["longitude"].mean()

    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=11,
        tiles="OpenStreetMap"
    )

    p_min = city_df["insurance_premium"].min()
    p_max = city_df["insurance_premium"].max()

    # Ensure ONE marker per locality
    unique_localities = city_df.drop_duplicates(subset=["locality_name"])

    # Fixed marker size by category (avoids overlap confusion)
    radius_map = {
        "green": 6,
        "orange": 8,
        "red": 10
    }

    for _, row in unique_localities.iterrows():
        color = premium_color(
            row["insurance_premium"],
            p_min,
            p_max
        )

        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=radius_map[color],
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=1.0,   # solid color → no blending
            popup=f"""
            <b>{row['locality_name']}</b><br>
            Premium: ₹{int(row['insurance_premium'])}<br>
            AQI: {row['avg_aqi']}<br>
            Flood Risk: {row['urban_flood_risk']}
            """
        ).add_to(m)

    return m
