import folium
import os

# Crear un mapa centrado en las coordenadas proporcionadas
mapa = folium.Map(location=[-41.46067771036199, -72.95166123635632], zoom_start=13)

# Guardar el mapa en un archivo HTML
# Obtener la ruta del archivo actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Crear la ruta completa para guardar el archivo HTML
file_path = os.path.join(current_dir, 'mapa.html')

# Guardar el mapa en el archivo HTML
mapa.save(file_path)
