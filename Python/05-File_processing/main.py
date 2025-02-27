
frutas = open("c:/Users/janov/Desktop/DataEngineer-RoadMap/Python/05-File_processing/files/fruits.txt")

content = frutas.read()

print(content)



# Otra forma de leer el archivo

with open("c:/Users/janov/Desktop/DataEngineer-RoadMap/Python/05-File_processing/files/fruits.txt") as frutas:
    content = frutas.read()
    print(content)



# Escribir en un archivo
with open("c:/Users/janov/Desktop/DataEngineer-RoadMap/Python/05-File_processing/files/countries.txt", "w") as countries:
    
    countries.write("Brasil\nChile\nArgentina\nPeru\nColombia\nMexico\nVenezuela\nUruguay\nParaguay\nEcuador\nBolivia\nPanama\nCosta Rica\nNicaragua\nHonduras\nEl Salvador\nGuatemala\nCuba\nPuerto Rico\nRepublica Dominicana\nHaiti\nJamaica\nTrinidad y Tobago\nBarbados\nBahamas\nBelice\nGuyana\nSurinam\nGuayana Francesa\n")
    
    

# Agregar contenido a un archivo existente
with open("c:/Users/janov/Desktop/DataEngineer-RoadMap/Python/05-File_processing/files/countries.txt", "a+") as countries:
    
    countries.write("Antigua y Barbuda\nSan Cristobal y Nieves\nSanta Lucia")
    countries.seek(0)
    content = countries.read()
    
print(content)    
    
    
    
    