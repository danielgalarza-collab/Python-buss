
def tres_mayores(numeros):
    # Ordenamos la lista de mayor a menor con sorted y reverse=True
    numeros_ordenados = sorted(numeros, reverse=True)
    
    # Tomamos solo los 3 primeros
    top3 = numeros_ordenados[:3]
    
    return top3

lista = [10, 4, 33, 7, 25, 99, 56]
print("Lista original:", lista)
print("Tres números mayores:", tres_mayores(lista))
