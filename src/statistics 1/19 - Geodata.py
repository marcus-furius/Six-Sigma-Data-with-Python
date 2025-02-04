import pandas as pd
import os
import folium
from folium.plugins import MarkerCluster

# Load the updated CSV file
data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
data_file = os.path.join(data_folder, 'Information Services.CSV')
df = pd.read_csv(data_file)

# Clean and process the Geolocation column to extract valid coordinates
def extract_coordinates(geo):
    try:
        lat, lon = geo.strip('()').split(',')
        return float(lat), float(lon)
    except (ValueError, AttributeError):
        return None, None

# Apply the extraction function
df['Latitude'], df['Longitude'] = zip(*df['Geolocation'].map(extract_coordinates))

# Filter valid locations
valid_locations = df.dropna(subset=['Latitude', 'Longitude'])

# Create a folium map centered on a global view
map_center = [40.0, -20.0]
map_folium = folium.Map(location=map_center, zoom_start=2)

# Add clustered markers for employee locations
marker_cluster = MarkerCluster().add_to(map_folium)

for _, row in valid_locations.iterrows():
    location = [row['Latitude'], row['Longitude']]
    popup_info = f"""
    <b>Name:</b> {row['Name']}<br>
    <b>State Code:</b> {row['State Code'] or row['Country']}<br>
    <b>Country:</b> {row['Country']}
    """
    
    # Add circular marker with popup
    folium.Circle(
        location=location,
        radius=50000,  # Radius in meters
        color="blue" if row['State Code'] else "green",
        fill=True,
        fill_color="blue" if row['State Code'] else "green",
        fill_opacity=0.5,
        tooltip="Click for more info",
        popup=folium.Popup(popup_info, max_width=300)
    ).add_to(map_folium)
    
    # Add markers to the cluster
    folium.Marker(
        location=location,
        icon=folium.Icon(color="red" if row['State Code'] else "green"),
        popup=folium.Popup(popup_info, max_width=300)
    ).add_to(marker_cluster)

# Save the map to an HTML file
data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
output_path = os.path.join(data_folder, 'IS_fte_locations_map.html')
map_folium.save(output_path)

print(f"Map saved to {output_path}")
