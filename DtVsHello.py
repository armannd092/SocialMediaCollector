import pandas as pd
import folium
import json
from folium import plugins
import os

fp = os.path.join('csv', 'Infraestructures_Inventari_Reserves.csv')
gj = os.path.join('geojson', 'ZONES30_POLIGONS.geojson')
gj_b = os.path.join('geojson', 'VIES_CICLABLES.geojson')


parking_data = pd.read_csv(fp)
lng = parking_data['Longitud'].astype(float)
ltd = parking_data['Latitud'].astype(float)
rds = parking_data['Numero_Places'].astype(float)
folium_map = folium.Map(location=[41.389285, 2.168330],
                        zoom_start=13,
                        tiles="cartodbpositron")
n = len(lng)
for i in range(n-1):
    #folium.vector_layers.Marker(location=[ltd[i], lng[i]])
    folium.vector_layers.Circle(location=[ltd[i], lng[i]],
                                radius=0.2,
                                color='#ACDEE0',
                                fill=True,
                                fill_color='#ACDEE0',
                                opacity=0.4
                                ).add_to(folium_map)

folium.GeoJson(gj,
               style_function=lambda x: {'Color': '#007F73' ,'weight': 0}
               ).add_to(folium_map)
folium.GeoJson(gj_b,
                style_function=lambda x: {'fillColor': '#B50046', 'Color': '#C6527F' ,'weight': 1}
               ).add_to(folium_map)

plugins.fullscreen.Fullscreen(position='bottomright',
                                title='Expand me',
                                title_cancel='Exit me',
                                force_separate_button=True)

#plugins.heat_map.HeatMap([parking_data['Longitud'],parking_data['Latitud']],'parking',gradient={.4: 'blue', .65: 'lime', 1: 'red'}).add_to(folium_map)





#folium.CircleMarker(location=[ltd[0], lng[0]],radius=5,fill=True).add_to(folium_map)

folium_map.save("map1.html")