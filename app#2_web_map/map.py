import folium
import pandas
import json

data = pandas.read_csv("Volcanoes.txt")
lat = data["LAT"]
lon = data["LON"]
name = data["NAME"]
elev = data["ELEV"]

def definition_of_color(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 2000:
        return "pink"
    else:
        return "black"

map = folium.Map(location=[38.6, -99], zoom_start=6, tiles="Stamen Terrain")
#making feature froup to use several methods at the same time
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    # format of popup windows
    # iframe = folium.IFrame(html=f"{nm}  ({el}m)", width=200, height=50)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=7, popup=str(el)+" m", fill_color=definition_of_color(el), color="grey", fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save('us_volcanoes.html')