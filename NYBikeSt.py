import folium
import folium.plugins.polyline_text_path
import pandas as pd
import numpy as np

fp = r'C:\Users\arman\Downloads\Compressed\Bike\BikeAdiction\tripNum_Station_loc.csv'
fp_end = r'C:\Users\arman\Downloads\Compressed\Bike\BikeAdiction\end_tripNum_Station_loc.csv'
data = pd.read_csv(fp_end, encoding='utf-8',dtype='str')
lon = list(np.array(data['latitude']))
lat = list(np.array(data['longitude']))
rad = list(np.array(data['TripNum']))
n = len(lat)-1
d =[]
for i in range(n):
    d.append([float(lon[i]), float(lat[i]),float(rad[i])])
    pass
st = folium.plugins.HeatMap(d,min_opacity=0.3,radius=13,blur=18)
print(d)

folium_map = folium.Map(location=[40.779671,-73.955504],
                        zoom_start=12,
                        tiles='https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png',
                        attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>')
'''
bike = folium.map.FeatureGroup(name='BikeSt')
for i in range(n):

    location = [float(lon[i]), float(lat[i])]
    folium.vector_layers.Circle(location=location,radius=int(rad[i])/80,
                                        color = '#FF548D',
                                        fill = True,
                                        fill_color = '#FF548D',
                                        opacity = 0.7,
                                        weight=1,

    ).add_to(bike)

bike.add_to(folium_map)'''
st.add_to(folium_map)
folium_map.save("end_TripNumST.html")
