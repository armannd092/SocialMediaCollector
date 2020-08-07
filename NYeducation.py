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
                                              color='#0059BD',
                                              fill=True,
                                              fill_color='#0059BD',
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


#gj= os.path.join('geojson','Primary-Commercial-Zoning-by-lot.geojson')
#gj2 = os.path.join('geojson','Subway-Stations.geojson')
#gj10 = os.path.join('geojson','Bicycle Parking Shelters.geojson')
#gj11 = os.path.join('geojson','Bus Stop Shelters.geojson')
#gj3 = os.path.join('geojson','Primary-Residential-Zoning-by-lot.geojson')
#gj4 = os.path.join('geojson','PublicPlazas.geojson')
#gj5 = os.path.join('geojson','Pavement-Edge.geojson')
#gj6 = os.path.join('geojson','Parking Lot.geojson')
gj7 = os.path.join('geojson','Colleges-Universities.geojson')
gj13 = os.path.join('geojson','Schools.geojson')
gj14 = os.path.join('geojson','Library.geojson')
#gj8 = os.path.join('geojson','OpenSpace(Parks).geojson')
#gj9 = os.path.join('geojson','Building-Footprints.geojson')
'''os.path.normpath(gj)
os.path.normpath(gj2)
os.path.normpath(gj3)
os.path.normpath(gj4)
os.path.normpath(gj5)
os.path.normpath(gj6)

os.path.normpath(gj8)
os.path.normpath(gj9)
dgj7 = json.load(open(gj7)
os.path.normpath(gj10)
os.path.normpath(gj11)
dgj2 = json.load(open(gj2))
dgj10 = json.load(open(gj10))
dgj11 = json.load(open(gj11)))
os.path.normpath(gj2)
'''
os.path.normpath(gj7)
os.path.normpath(gj13)
os.path.normpath(gj14)
dgj7 = json.load(open(gj7))
dgj13 = json.load(open(gj13))
dgj14 = json.load(open(gj14))

def create_map(tiles='https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png',attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'):
    return folium.Map(location=[40.779671,-73.955504],zoom_start=12, tiles= tiles,attr=attr, prefer_canvas=True)


folium_map = create_map()
minimap = folium.plugins.MiniMap(toggle_display=True,
                                 position='bottomleft',
                                 zoom_level_offset=-4,
                                 width=200, height=200,
                                 tile_layer= 'cartodbpositron')

'''comers = folium.map.FeatureGroup(name='Commercial')
folium.GeoJson(data=gj,
                style_function=lambda feature:{
                  'fillColor': '#FFA8CA',
                  'color': '#D77DAF',
                  'weight': 0.2,
                  'opacity': 1
                  }
                ).add_to(comers)

rdl = folium.map.FeatureGroup(name='Residential')
folium.GeoJson(data=gj3,
                style_function=lambda feature:{
                  'fillColor': '#A5F7FF',
                  'color': '#5CBAC3',
                  'weight': 0.2,
                  'opacity': 1
                  }
                ).add_to(rdl)
plt = folium.map.FeatureGroup(name='Parking')
folium.GeoJson(data=gj6,
                style_function=lambda feature:{
                  'fillColor': '#080037',
                  'color': '#EBE4FF',
                  'weight': 0.2,
                  }
                ).add_to(plt)


plaza = folium.map.FeatureGroup(name='plaza')
folium.GeoJson(data=gj4,
                style_function=lambda feature:{
                  'fillColor': '#FFB32D',
                  'color': '#FFE6B9',
                  'weight': 0.4,
                  }
                ).add_to(plaza)

opsp = folium.map.FeatureGroup(name='OpenSpace(park)')
folium.GeoJson(data=gj8,
                style_function=lambda feature:{
                  'fillColor': '#D2DD30',
                  'color': '#5F6500',
                  'weight': 0.4,
                  }
                ).add_to(opsp)
bft = folium.map.FeatureGroup(name='Building Footprint')
folium.GeoJson(data=gj9,
                style_function=lambda feature:{
                  'color': '#484848',
                  'weight': 0.1,
                  }
                ).add_to(bft)

sw = folium.map.FeatureGroup(name='SideWalk')AA
folium.GeoJson(data=gj5,
                style_function=lambda feature:{
                  'color': '#27BFB5',
                  'weight': 0.2,
                  'opacity': 1
                  }
                ).add_to(sw)

mts = folium.map.FeatureGroup(name='MetroStation')
for feature in dgj2['features']:
    if feature['geometry']['type'] == 'Point':
        loc = feature['geometry']['coordinates']
        popup = feature['properties']['name']
        #folium.Marker(location=[loc[1],loc[0]],popup=popup,icon=metro_icon).add_to(mts)
        folium.vector_layers.CircleMarker(location=[loc[1],loc[0]],
                                    radius=5,
                                    color='#45B39D',
                                    fill=True,
                                    fill_color='#45B39D',
                                    opacity=1,
                                    popup=popup).add_to(mts)



bus = folium.map.FeatureGroup(name='Bus shelter')
for feature in dgj11['features']:
    if feature['geometry']['type'] == 'Point':
        loc = feature['geometry']['coordinates']
        popup = feature['properties']['location']
        folium.vector_layers.CircleMarker(location=[loc[1],loc[0]],
                                    radius=1,
                                    color='#D35400',
                                    fill=True,
                                    fill_color='#D35400',
                                    opacity=0.7,
                                    popup=popup).add_to(bus)

bike = folium.map.FeatureGroup(name='Bike parking')
for feature in dgj10['features']:
    if feature['geometry']['type'] == 'Point':
        loc = feature['geometry']['coordinates']
        #popup = feature['properties']['name']
        folium.vector_layers.CircleMarker(location=[loc[1],loc[0]],
                                    radius=3,
                                    color='#FCD3CB',
                                    fill=True,
                                    fill_color='#FCD3CB',
                                    opacity=0.7,
                                    ).add_to(bike)'''
uni = folium.map.FeatureGroup(name='Universities')
for feature in dgj7['features']:
    if feature['geometry']['type'] == 'Point':
        loc = feature['geometry']['coordinates']
        popup = feature['properties']['name']
        #folium.Marker(location=[loc[1],loc[0]],popup=popup,icon=metro_icon).add_to(mts)
        folium.vector_layers.CircleMarker(location=[loc[1],loc[0]],
                                    radius=15,
                                    color='#A93226',
                                    fill=True,
                                    fill_color='#A93226',
                                    opacity=1,
                                    popup=popup).add_to(uni)
school = folium.map.FeatureGroup(name='School')
for feature in dgj13['features']:
    if feature['geometry']['type'] == 'Point':
        loc = feature['geometry']['coordinates']
        popup = feature['properties']['SCH_TYPE']
        #folium.Marker(location=[loc[1],loc[0]],popup=popup,icon=metro_icon).add_to(mts)
        folium.vector_layers.CircleMarker(location=[loc[1],loc[0]],
                                    radius=2,
                                    color='#C39BD3',
                                    fill=True,
                                    fill_color='#C39BD3',
                                    opacity=1,
                                    popup=popup).add_to(school)
lib = folium.map.FeatureGroup(name='Library')
for feature in dgj14['features']:
    if feature['geometry']['type'] == 'Point':
        loc = feature['geometry']['coordinates']
        popup = feature['properties']['name']
        #folium.Marker(location=[loc[1],loc[0]],popup=popup,icon=metro_icon).add_to(mts)
        folium.vector_layers.CircleMarker(location=[loc[1],loc[0]],
                                    radius=10,
                                    color='#F7DC6F',
                                    fill=True,
                                    fill_color='#F7DC6F',
                                    opacity=1,
                                    popup=popup).add_to(lib)

'''comers.add_to(folium_map)
rdl.add_to(folium_map)

plaza.add_to(folium_map)
plt.add_to(folium_map)

opsp.add_to(folium_map)
#bft.add_to(folium_map)
#sw.add_to(folium_map)
mts.add_to(folium_map)
bus.add_to(folium_map)
bike.add_to(folium_map)'''
uni.add_to(folium_map)
school.add_to(folium_map)
lib.add_to(folium_map)
folium.LayerControl().add_to(folium_map)
minimap.add_to(folium_map)

'''folium.GeoJson(data=gj2,
                style_function=lambda feature:{

                  'fillColor': '#FFBAEA',
                  'color': '#FFBAEA',
                  'weight': 2,
                  'opacity': 0.8},
                    tooltip=folium.features.GeoJsonTooltip(fields=[name],
                                                           aliases=['station'],
                                                           labels=True,
                                                           sticky=True,
                                                           toLocaleString=True)

                ).add_to(folium_map)'''

plugins.fullscreen.Fullscreen(position='bottomright',
                                title='Expand me',
                                title_cancel='Exit me',
                                force_separate_button=True).add_to(folium_map)
draw = folium.plugins.Draw(export=True)
draw.add_to(folium_map)
folium.plugins.MeasureControl(position='bottomleft').add_to(folium_map)
sf = os.path.join('html','NYEducation.html')
folium_map.save(sf)

#html_txt = folium_map.get_root().render()