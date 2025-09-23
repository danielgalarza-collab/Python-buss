# Sirve para crear listas de forma compacta.
# Un comprehension en Python es una forma concisa de crear nuevas colecciones (listas, sets o diccionarios) aplicando transformaciones y filtros a iterables dentro de una sola expresión.
""""Los comprehensions  son una construcción especial del lenguaje que permite crear colecciones (listas, conjuntos o diccionarios) de forma concisa, legible y eficiente,
#  a partir de secuencias o iterables existentes, aplicando expresiones y condiciones en una sola línea.

#En lugar de usar un bucle for tradicional con métodos como .append(), los comprehensions permiten combinar iteración, filtrado y transformación de datos dentro de una sintaxis compacta.
"""
""""
[expresión for elemento in iterable if condición]
{expresión for elemento in iterable if condición}       # set
{clave: valor for elemento in iterable if condición}    # dict
"""
#expresión → lo que se quiere calcular o transformar.

#elemento → variable que recorre el iterable.

#iterable → cualquier objeto que se pueda recorrer (lista, rango, string, etc.).

# condición (opcional) → filtra qué elementos incluir.

#Tipos de Comprehensions
# 1. list comprehension : Genera listas nuevas
numeros = [1, 2, 3, 4, 5]
cuadrados = [n**2 for n in numeros]          # [1, 4, 9, 16, 25]
pares = [n for n in numeros if n % 2 == 0]   # [2, 4]

#2. Set Comprehension : Genera conjuntos (no admite duplicados)
numeros = [1, 2, 2, 3, 4]
cuadrados = {n**2 for n in numeros}   # {1, 4, 9, 16}

#3. Dictionary Comprehension
nombres = ["Ana", "Luis", "Pedro"]
longitudes = {nombre: len(nombre) for nombre in nombres}
# {'Ana': 3, 'Luis': 4, 'Pedro': 5}

#4. Nested comprehension (anidado) : permite recorrer estructuras mas complejas
matriz = [[1, 2], [3, 4], [5, 6]]
flatten = [num for fila in matriz for num in fila]
# [1, 2, 3, 4, 5, 6]

"""
Ventajas

✅ Sintaxis más compacta y legible.
✅ Más rápida que los bucles tradicionales en la mayoría de los casos.
✅ Permite expresar en una sola línea operaciones que normalmente ocuparían varias.

 Desventajas

⚠️ Si son demasiado complejas, pueden volverse difíciles de leer.
⚠️ No siempre son más rápidas si incluyen operaciones muy pesadas.
"""