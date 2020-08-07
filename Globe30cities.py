import folium
import folium.plugins.polyline_text_path
import pandas as pd
import numpy as np

fp = 'csv/My30Cities.csv'
data = pd.read_csv(fp, encoding='utf-8',dtype='str')
lon = list(np.array(data['Latitude']))
lat = list(np.array(data['Longitude']))
rad = list(np.array(data['Population (millions)']))
txt = list(np.array(data['Urban']))
n = len(lat)-1
folium_map = folium.Map(location=[0,0],
                        zoom_start=3,
                        tiles='https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png',
                        attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>')
city = folium.map.FeatureGroup(name='cityPo')
for i in range(n):

    location = [float(lon[i]), float(lat[i])]
    folium.vector_layers.Circle(location=location,radius=int(rad[i])*30000,
                                        color = '#FF8CB9',
                                        fill = True,
                                        fill_color = '#FF8CB9',
                                        opacity = 0.7,
                                        weight=1,
                                        popup=txt[i]
    ).add_to(city)

city.add_to(folium_map)
folium_map.save("globeRaw.html")