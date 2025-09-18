# ejercicio  
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

# Prime Checker con loop hasta que el usuario escriba "salir"
while True:
    numero = input("Escribe un numero para verificar si es primo(o escribe 'salir' para terminar: ").strip().lower() # aca preguntamos al usuario que escriba el numero , y strip es para eliminar los espacios en blanco

    if numero == "salir":
        print("saliendo del programa")
        break 
    if not numero.isdigit():
        print("Entrada invalida. Debes escribir un numero \n")
        continue

    numero = int(numero) # aca pasamos el imput a numero entero

    if numero < 2:
        print(f"{numero} no es primo (los numeros primos son mayores que 1). \n")
        continue

    es_primo = True # variable para marcar si es primo

    # Recorremos desde 2 hasta la raiz cuadrada del número
    for i in range (2, numero):
        if numero % i == '0':
            es_primo = False
            break
    
    if es_primo:
        print(f"{numero} es un numero primo")
    else:
        print(f"{numero} no es primo ")