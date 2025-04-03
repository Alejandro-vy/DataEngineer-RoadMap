from math import sqrt

# Resumen de errores principales en Python con ejemplos:

# 1. SyntaxError: Error de sintaxis
# Ocurre cuando el código no sigue las reglas de la sintaxis de Python.
# Ejemplo:
# if True
#     print("Error de sintaxis")

# Corrección:
if True:
    print("Error corregido")

# 2. NameError: Nombre no definido
# Ocurre cuando se intenta usar una variable o función que no existe.
# Ejemplo:
# print(variable_no_definida)

# Corrección:
variable_definida = "Ahora está definida"
print(variable_definida)

# 3. TypeError: Tipo de dato incorrecto
# Ocurre cuando se realiza una operación con tipos incompatibles.
# Ejemplo:
# resultado = "Texto" + 5

# Corrección:
resultado = "Texto" + str(5)
print(resultado)

# 4. IndexError: Índice fuera de rango
# Ocurre cuando se intenta acceder a un índice inexistente en una lista.
# Ejemplo:
# lista = [1, 2, 3]
# print(lista[5])

# Corrección:
lista = [1, 2, 3]
if len(lista) > 5:
    print(lista[5])
else:
    print("Índice fuera de rango")

# 5. KeyError: Clave inexistente en un diccionario
# Ocurre cuando se intenta acceder a una clave que no existe.
# Ejemplo:
# diccionario = {"clave": "valor"}
# print(diccionario["clave_inexistente"])

# Corrección:
diccionario = {"clave": "valor"}
print(diccionario.get("clave_inexistente", "Clave no encontrada"))

# 6. ValueError: Valor inválido
# Ocurre cuando una función recibe un argumento con un valor inapropiado.
# Ejemplo:
# numero = int("texto")

# Corrección:
try:
    numero = int("texto")
except ValueError:
    print("No se puede convertir 'texto' a entero")

# 7. AttributeError: Atributo inexistente
# Ocurre cuando se intenta acceder a un atributo que no existe en un objeto.
# Ejemplo:
# texto = "Hola"
# texto.append("!")

# Corrección:
texto = "Hola"
texto = texto + "!"
print(texto)

# 8. ImportError: Módulo o función no encontrado
# Ocurre cuando se intenta importar un módulo o función inexistente.
# Ejemplo:
# from math import inexistente

# Corrección:
print(sqrt(16))