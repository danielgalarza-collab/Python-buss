#1 .A partir de la lista [1, 2, 3, 4, 5], genera una nueva lista con los cuadrados de cada número.
numero = [1,2,3,4,5]
cuadrados = [n**2 for n in numero]
print(cuadrados)

#2. Crea una lista con los números pares del 1 al 20 usando range()
numeros_pares = list(range(2,21,2))
print(numeros_pares)
""""
2: El número de inicio (el primer número par en nuestro rango).
21: El número de fin (el rango no incluye este número, por lo que va hasta 20).
2: El paso, que indica que debe saltar de 2 en 2, obteniendo así solo los pares.
"""
# 3.Set Comprehensions : A partir de una lista con números repetidos, crea un set de los cuadrados (sin repetidos).
numeros = [1, 2, 2, 3, 4, 4, 5]
cuadrados = [n**2 for n in numeros]
print(numero)

#4. set comprehensions : Genera un set con las vocales que aparecen en la palabra "programacion".
vocales = "aeiou"
palabra = "programacion"
vocales_palabra = {n for n in palabra if n in "aeiou" }
print(vocales_palabra)

#5. Dada una lista de nombres, crea un diccionario con el nombre como clave y su longitud como valor.
nombres = ["Ana", "Luis", "Pedro"]
longitud = {nombre: len(nombre) for nombre in nombres}
print(longitud)

#6.A partir de un diccionario con precios de productos, genera otro que solo incluya los productos con precio mayor a 100.
precios = {"pan": 50, "carne": 200, "queso": 150, "agua": 30}
PrecioMayor100 = {producto: precio for producto, precio in precios.items() if precio > 100}
print(PrecioMayor100)

# 7.Obtener solo los nombres de los usuarios activos
usuarios = [
    {"id": 1, "nombre": "Ana", "activo": True},
    {"id": 2, "nombre": "Luis", "activo": False},
    {"id": 3, "nombre": "Pedro", "activo": True}
]
activos = [u["nombre"] for u in usuarios if u ["activo"]]
print(activos)