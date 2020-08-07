import pandas as pd
import folium
from folium import plugins
import os

fp = os.path.join('csv', 'Sheet1.csv')

print(fp)


gab_data = pd.read_csv(fp)
lng = gab_data['lon'].astype(float)
ltd = gab_data['lat'].astype(float)
rds = gab_data['total'].astype(float)
folium_map = folium.Map(location=[-0.960856, 119.870564],
                        zoom_start=10,
                        tiles="cartodbpositron")

n = len(lng)
"""
for i in range(n-1):
    #folium.vector_layers.Marker(location=[ltd[i], lng[i]])
    folium.vector_layers.Circle(location=[ltd[i], lng[i]],
                                radius=rds[i],
                                color='#ACDEE0',
                                fill=True,
                                fill_color='#ACDEE0',
                                opacity=0.4
                                ).add_to(folium_map)"""

heat_data = [[[row['lat'],row['lon']] for index, row in gab_data[gab_data['total'] == i].iterrows()] for i in range(0,n)]

hm = plugins.HeatMapWithTime(heat_data,auto_play=True,max_opacity=0.8)
hm.add_to(folium_map)
plugins.fullscreen.Fullscreen(position='bottomright',
                                title='Expand me',
                                title_cancel='Exit me',
                                force_separate_button=True)


folium_map.save("gabheatmap.html")