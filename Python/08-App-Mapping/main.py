import folium
#print(folium.__version__)
import os

import pandas 

data = pandas.read_csv("c:/Users/janov/Desktop/DataEngineer-RoadMap/Python/08-App-Mapping/Files/Volcanoes.txt")

lat = list(data["LAT"])

lon = list(data["LON"])

# Crear un mapa centrado en las coordenadas proporcionadas
mapa = folium.Map(location=[38.58, -99.09], zoom_start=10) 

fg = folium.FeatureGroup(name="Mi Mapa")



folium.TileLayer(
     tiles='https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg',
     attr='Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap contributors',
    name='Stamen Terrain'
 ).add_to(mapa)





for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup='marker', icon=folium.Icon(color="blue")))




mapa.add_child(fg)















# Obtener la ruta del archivo actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Crear la ruta completa para guardar el archivo HTML
file_path = os.path.join(current_dir, 'mapa.html')

# Guardar el mapa en el archivo HTML
mapa.save(file_path)
