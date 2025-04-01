import folium
#print(folium.__version__)
import os

import pandas 

import json


data = pandas.read_csv("c:/Users/janov/Desktop/DataEngineer-RoadMap/Python/08-App-Mapping/Files/Volcanoes.txt")

lat = list(data["LAT"])

lon = list(data["LON"])

elev = list(data["ELEV"])

def color_producer(elevation):
    
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


# Crear un mapa centrado en las coordenadas proporcionadas
mapa = folium.Map(location=[38.58, -99.09], zoom_start=10) 

fgv = folium.FeatureGroup(name="Volcanoes")


folium.TileLayer(
     tiles='https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg',
     attr='Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap contributors',
    name='Stamen Terrain'
 ).add_to(mapa)




for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(
        location=[lt, ln],
        radius=7,
        popup=folium.Popup(str(el) + "m", parse_html=True),
        fill_color=color_producer(el),
        color='grey',
        fill=True,
        fill_opacity=0.7
    ))


fgp = folium.FeatureGroup(name="Population")


with open("c:/Users/janov/Desktop/DataEngineer-RoadMap/Python/08-App-Mapping/Files/world.json", 'r', encoding='utf-8-sig') as file:
    geo_data = json.load(file)

# Filter out features with missing geometries
geo_data['features'] = [feature for feature in geo_data['features'] if feature.get('geometry') is not None]

fgp.add_child(folium.GeoJson(
    data=geo_data, style_function=lambda x: {
        'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 
                     'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 
                     'red'}
))




mapa.add_child(fgv)

mapa.add_child(fgp)

mapa.add_child(folium.LayerControl())













# Obtener la ruta del archivo actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Crear la ruta completa para guardar el archivo HTML
file_path = os.path.join(current_dir, 'mapa.html')

# Guardar el mapa en el archivo HTML
mapa.save(file_path)
