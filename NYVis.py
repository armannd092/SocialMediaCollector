import json
import folium
from folium import plugins
from ipywidgets import interact
import os
import htmlmin

def datalayer(fn,color):
    fgj = os.path.join('geojson', fn)
    os.path.normpath(fgj)
    dgj = json.load(open(fgj))
    f = folium.map.FeatureGroup(name= fn)
    for feature in dgj['features']:
        if feature['geometry']['type'] == 'Point':
            loc = feature['geometry']['coordinates']
            popup = feature['properties']['name']
            # folium.Marker(location=[loc[1],loc[0]],popup=popup,icon=metro_icon).add_to(mts)
            folium.vector_layers.CircleMarker(location=[loc[1], loc[0]],
                                              radius=3,
                                              color=color,
                                              fill=True,
                                              fill_color=color,
                                              opacity=0.7,
                                              popup=popup).add_to(f)
            pass
        else:
            folium.GeoJson(data=gj,
                           style_function=lambda feature: {
                               'fillColor': color,
                               'color': color,
                               'weight': 0.2,
                               'opacity': 1
                           }
                           ).add_to(f)
            pass
    return f
2
def create_map(tiles="cartodbpositron"):

    return folium.Map(location=[40.779671,-73.955504],
                      min_lat=min(-74.964661,-73.921011),
                      max_lat=max(-74.964661,-73.921011),
                      min_lon=min(40.324497,41.173346),
                      max_lon=max(40.324497,41.173346),
                      zoom_start=12,
                      min_zoom=8,
                      max_zoom=16,
                      tiles= tiles)


if __name__=='__main__':
    map = create_map()


for file in os.listdir('geojson'):

    if file.endswith('.geojson'):
        print(file)

