import folium

folium_map = folium.Map(location=[40.779671,-73.955504],
                        zoom_start=13,
                        tiles='https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png',
                        attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>')

folium_map.save("mapnewyorkDark.html")