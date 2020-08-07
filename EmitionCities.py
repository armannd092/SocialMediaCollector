import folium
import folium.plugins.polyline_text_path
import pandas as pd
import numpy as np

fpData = 'csv/UNdata_Export_20190918_212803620.csv'
fpCities = 'csv/worldcities.csv'

data = pd.read_csv(fpData, encoding='utf-8',dtype='str')
cities = pd.read_csv(fpCities, encoding='utf-8',dtype='str')
citiescls  = pd.DataFrame.drop(cities,columns=["city_ascii","country","iso2","iso3","admin_name","capital","population","id"])
citiescls.set_index('city')
datacls =  pd.DataFrame.drop(data,columns='Year')
df=[]
for c in datacls['Country or Area']:
    print(citiescls.get_value(citiescls[citiescls['city']==c].index[0],col='lat'))
    #df.append(citiescls[citiescls['city'] == c].index)
#print(df)
'''lon = list(np.array(data['Latitude']))
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
folium_map.save("globeRaw.html")'''