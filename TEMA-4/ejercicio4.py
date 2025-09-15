
def tres_mayores(numeros):
    # Ordenamos la lista de mayor a menor con sorted y reverse=True
    numeros_ordenados = sorted(numeros, reverse=True)
    
    # Tomamos solo los 3 primeros
    top3 = numeros_ordenados[:3]
    
    return top3

lista = [10, 4, 33, 7, 25, 99, 56]
print("Lista original:", lista)
print("Tres números mayores:", tres_mayores(lista))

#Ejercicio de estudiantes y el promedio en las notas 
estudiantes = [
    ("Ana", [7, 8, 9]),
    ("Luis", [5, 6, 7, 8]),
    ("María", [10, 9]),
    ("Pedro", [4, 6, 5])
]

# Calculamos el promedio de cada estudiante
promedios = []
for nombre, notas in estudiantes:
    promedio = sum(notas) / len(notas)
    promedios.append((nombre, promedio))

# Ordenamos la lista de mayor a menor promedio
promedios.sort(key=lambda x: x[1], reverse=True)


print("Lista de promedios:", promedios)

# Mostramos el mejor estudiante
mejor = promedios[0]
print(f"El mejor estudiante es {mejor[0]} con un promedio de {mejor[1]:.1f}")
