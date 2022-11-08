import folium
import pandas as pd

# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42

# Create map and display it
san_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# Read Dataset 
cdata = pd.read_csv('https://cocl.us/sanfran_crime_dataset')
cdata.head()

# get the first 200 crimes in the cdata
limit = 200
data = cdata.iloc[0:limit, :]

# Instantiate a feature group for the incidents in the dataframe
incidents = folium.map.FeatureGroup()

# Loop through the 200 crimes and add each to the incidents feature group
for lat, lng, in zip(cdata.Y, data.X):
    incidents.add_child(
        folium.CircleMarker(
            [lat, lng],
            radius=7, # define how big you want the circle markers to be
            color='yellow',
            fill=True,
            fill_color='red',
            fill_opacity=0.4
        )
    )

# Add incidents to map
san_map = folium.Map(location=[latitude, longitude], zoom_start=12)
san_map.add_child(incidents)

# add pop-up text to each marker on the map
latitudes = list(data.Y)
longitudes = list(data.X)
labels = list(data.Category)

for lat, lng, label in zip(latitudes, longitudes, labels):
    folium.Marker([lat, lng], popup=label).add_to(san_map)    
    
# add incidents to map
san_map.add_child(incidents)

# Display the map of San Francisco
san_map.save('1.html')
