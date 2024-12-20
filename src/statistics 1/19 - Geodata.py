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

# Group by location and aggregate employee names
location_employee_data = valid_locations.groupby(['Latitude', 'Longitude']).agg({
    'Name': lambda x: ', '.join(x)
}).reset_index()

# Create a folium map centered on a global view
map_center = [40.71, -74.01]
map_folium = folium.Map(location=map_center, zoom_start=5)

# Add a marker cluster to the map
marker_cluster = MarkerCluster().add_to(map_folium)

# Add markers for each location with the employee count and names
for _, row in location_employee_data.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"Employees: {len(row['Name'].split(', '))}<br>Names: {row['Name']}",
    ).add_to(marker_cluster)

# Save the map to an HTML file
data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
output_path = os.path.join(data_folder, 'IS_fte_locations_map.html')
map_folium.save(output_path)

print(f"Map saved to {output_path}")
