#For loops

paises = ["Chile", "Argentina", "Brasil", "Uruguay", "Paraguay", "Bolivia", "Peru", "Ecuador", "Colombia", "Venezuela"]


for pais in paises:
    print(pais)



capitales_norte_america = {"Mexico": "CDMX", 
                           "Canada": "Ottawa", 
                           "USA": "Washington DC"}


for pais, capital in capitales_norte_america.items():
    print(f"La capital de {pais} es {capital}")
    
    

# While loops

usuario = ""   

while usuario != "salir":
    usuario = input("Ingrese el usuario prohibido para salir: ") 