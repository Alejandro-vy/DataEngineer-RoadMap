import folium
print(folium.__version__)
import os

# Crear un mapa centrado en las coordenadas proporcionadas
mapa = folium.Map(location=[-41.46067771036199, -72.95166123635632], zoom_start=13) 

folium.TileLayer(
    tiles='https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg',
    attr='Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap contributors',
    name='Stamen Terrain'
).add_to(mapa)


add_child = folium.Marker(location=[-41.46067771036199, -72.95166123635632], 
                          popup='Casa de la Cultura', icon= folium.Icon(color="blue")).add_to(mapa)

# Obtener la ruta del archivo actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Crear la ruta completa para guardar el archivo HTML
file_path = os.path.join(current_dir, 'mapa.html')

# Guardar el mapa en el archivo HTML
mapa.save(file_path)
