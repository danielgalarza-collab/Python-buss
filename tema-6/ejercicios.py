# ejercicio final 
#  Prime checker with loop until user quits.

# Set para guardar números palíndromos únicos
palindromos = set()

# Diccionario para guardar todos los números y su estado
resultados = {}

# Bucle principal
while True:
    entrada = input("Introduce un número (o 'salir' para terminar): ").strip().lower()

    if entrada == "salir":
        break  # termina el bucle

    # Validación: verificar que sea un número válido
    if not entrada.isdigit():
        print("Por favor, introduce solo números.\n")
        continue

    # Comprobamos si el número es palíndromo
    es_palindromo = entrada == entrada[::-1]

    # Si es palíndromo, agregamos al set
    if es_palindromo:
        palindromos.add(entrada)

    # Guardamos en el diccionario
    resultados[entrada] = "palíndromo" if es_palindromo else "no palíndromo"

# Mostrar resultados
print("\nNúmeros palíndromos únicos ingresados:", palindromos)
print("Todos los resultados:", resultados)
