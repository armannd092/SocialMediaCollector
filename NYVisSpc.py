import json
import folium
from folium import plugins
from ipywidgets import interact
import os

'''gj = os.path.join('geojson','New York City Art Galleries.geojson')
gj2 = os.path.join('geojson','New York City Museums.geojson')
gj3 = os.path.join('geojson','Schools.geojson')
#gj4 = os.path.join('geojson','PublicPlazas.geojson')
#gj5 = os.path.join('geojson','Pavement-Edge.geojson')
#gj6 = os.path.join('geojson','Parking Lot.geojson')
gj7 = os.path.join('geojson','Colleges-Universities.geojson')
#gj8 = os.path.join('geojson','OpenSpace(Parks).geojson')
#gj9 = os.path.join('geojson','Building-Footprints.geojson')
os.path.normpath(gj)
os.path.normpath(gj3)
os.path.normpath(gj2)
#os.path.normpath(gj5)
#os.path.normpath(gj6)
os.path.normpath(gj7)
#os.path.normpath(gj8)
#os.path.normpath(gj9)
dgj2 = json.load(open(gj2))
dgj = json.load(open(gj))
dgj3 = json.load(open(gj3))
dgj7 = json.load(open(gj7))'''


tiles = [name.strip() for name in """
    OpenStreetMap
    Mapbox Bright
    Mapbox Control Room
    Stamen Terrain
    Stamen Toner
    Stamen Watercolor
    CartoDB positron
    CartoDB dark_matter
""".strip().split('\n')]

@interact(tiles = tiles)
def create_map(tiles="cartodbpositron"):
    return folium.Map(location=[40.779671,-73.955504],zoom_start=12, tiles= tiles, prefer_canvas=True)


folium_map = create_map()
minimap = folium.plugins.MiniMap(toggle_display=True,
                                 position='bottomleft',
                                 zoom_level_offset=-4,
                                 width=200, height=200,
                                 tile_layer= 'cartodbpositron')



'''uni = folium.map.FeatureGroup(name='University')
for feature in dgj7['features']:
    if feature['geometry']['type'] == 'Point':
        loc = feature['geometry']['coordinates']
        popup = feature['properties']['name']
        #folium.Marker(location=[loc[1],loc[0]],popup=popup,icon=metro_icon).add_to(mts)
        folium.vector_layers.CircleMarker(location=[loc[1],loc[0]],
                                    radius=2,
                                    color='#00B2C4',
                                    fill=True,
                                    fill_color='#00B2C4',
                                    opacity=0.7,
                                    popup=popup).add_to(uni)

gly = folium.map.FeatureGroup(name='Gallery')
for feature in dgj['features']:
    if feature['geometry']['type'] == 'Point':
        loc = feature['geometry']['coordinates']
        popup = feature['properties']['name']
        #folium.Marker(location=[loc[1],loc[0]],popup=popup,icon=metro_icon).add_to(mts)
        folium.vector_layers.CircleMarker(location=[loc[1],loc[0]],
                                    radius=2,
                                    color='#7900CA',
                                    fill=True,
                                    fill_color='#7900CA',
                                    opacity=0.7,
                                    popup=popup).add_to(gly)

msm = folium.map.FeatureGroup(name='Museums')
for feature in dgj2['features']:
    if feature['geometry']['type'] == 'Point':
        loc = feature['geometry']['coordinates']
        popup = feature['properties']['name']
        #folium.Marker(location=[loc[1],loc[0]],popup=popup,icon=metro_icon).add_to(mts)
        folium.vector_layers.CircleMarker(location=[loc[1],loc[0]],
                                    radius=2,
                                    color='#CA009B',
                                    fill=True,
                                    fill_color='#CA009B',
                                    opacity=0.7,
                                    popup=popup).add_to(msm)

schl = folium.map.FeatureGroup(name='Schools')
for feature in dgj3['features']:
    if feature['geometry']['type'] == 'Point':
        loc = feature['geometry']['coordinates']
        popup = feature['properties']['SCH_TYPE']
        print(loc)
        #folium.Marker(location=[loc[1],loc[0]],popup=popup,icon=metro_icon).add_to(mts)
        folium.vector_layers.CircleMarker(location=[loc[1],loc[0]],
                                    radius=2,
                                    color='#CF0000',
                                    fill=True,
                                    fill_color='#CF0000',
                                    opacity=0.7,
                                    popup=popup).add_to(schl)



schl.add_to(folium_map)
uni.add_to(folium_map)
msm.add_to(folium_map)
gly.add_to(folium_map)'''

folium.LayerControl().add_to(folium_map)
minimap.add_to(folium_map)

plugins.fullscreen.Fullscreen(position='bottomright',
                                title='Expand me',
                                title_cancel='Exit me',
                                force_separate_button=True).add_to(folium_map)
draw = folium.plugins.Draw(export=True)
draw.add_to(folium_map)
folium.plugins.MeasureControl(position='bottomleft').add_to(folium_map)
sf = os.path.join('html','mapRaw.html')
folium_map.save(sf)