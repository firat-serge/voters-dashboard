import requests
import folium

# define the URL of the GeoJSON API for Turkey's electoral map
url = 'http://127.0.0.1:5000/votes_geojson'

# send a GET request to the API and retrieve the GeoJSON data
response = requests.get(url)
data = response.json()

# create a map object using the first feature's coordinates as the initial center
center = [39.925533, 32.866287] # Turkey's center coordinates
m = folium.Map(location=center, zoom_start=6)

# add each feature to the map as a GeoJSON layer with custom style
for feature in data['features']:
    color = '#FF0000' if feature['properties']['kazanan'] == 'AKP_per' else '#0000FF' # custom color based on winner party
    style_function = lambda x: {'fillColor': color, 'color': 'black', 'weight': 1, 'fillOpacity': 0.7} # custom style
    folium.GeoJson(feature, style_function=style_function).add_to(m)

# display the map in a new window or inline in a Jupyter Notebook
m
