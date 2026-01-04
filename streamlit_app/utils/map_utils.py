import folium

def create_map(city_df):
    lat = city_df["latitude"].mean()
    lon = city_df["longitude"].mean()

    m = folium.Map(
        location=[lat, lon],
        zoom_start=11,
        tiles="OpenStreetMap"
    )

    for _, row in city_df.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=6,
            popup=f"""
            <b>{row['locality_name']}</b><br>
            Premium: ₹{int(row['insurance_premium'])}
            """,
            color="red",
            fill=True,
            fill_opacity=0.7
        ).add_to(m)

    return m
