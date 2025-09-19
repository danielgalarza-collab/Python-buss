# Función es un bloque de código autónomo que se ejecuta cuando lo llamamos
# Nos va a servir para atomizar y reutilizar código optimizando el mismo

# Parámetros son la lista de variables dentro de los paréntesis
# Argumentos son los valores que le enviamos a la función cuando es llamada

#EJEMPLO CLARO Y SENCILLO
def funcion(profesor,curso): #esto son los parametros que tendremos que introducir cuando llamemos a la funcion 
    print(f"El curso de {curso} lo dara el profesor {profesor}")

print("DANIEL GALARZA" , "CURSO DE PYTHON") #ESTOS SON LOS ARGUMENTOS QUE PONEMOS CUANDO LLAMEMOS A LA FUNCION 


def funcion2(profesor, curso, femenino):
    profesion = "el profesor"
    if femenino:
        profesion = "la profesora"
    print(f"El curso de {curso} lo dará {profesion} {profesor}")

          # Argumetos = valores
funcion2("Daniel", "Python desde Cero", False)
funcion2("Pedrito", "Cocina", False)
funcion2("Marina", "Manejo", True)
funcion2("Mercedes", "Bajo", True)

# Argumentos Arbitrarios (mandar múltiples argumentos según dependa)
# Hay que tener cuidado de que esté bien manejado para no dar errores

def llamar_alumnos(*alumnos):
    print(f"Mi mejor alumno es {alumnos[0]}")# coje el alumno segun el indice que pongamos 
    print(f"Mi alumna más divertida es {alumnos[2]}")

llamar_alumnos("Ricardo", "Antonieta", "Beatriz", "Lionel")

# Argumento clave / key arguments

def cursos(curso1, curso2, curso3):
    print(f"El primer curso que daré será el de {curso1}")
    print(f"el siguiente será el curso de {curso2}")
    print(f"y para finalizar daré el curso de {curso3}")

cursos(curso3 = "Java", curso2 = "CSS", curso1 = "HTML") # Indicaremos a que paráemtro corresponde cada argumento

# Argumentos claves arbitrarios

def llamar_alumno(**alumno):
    print(f"El apellido del alumno es {alumno["apellido"]}, y su nombre es {alumno["nombre"]}")

llamar_alumno(apellido = "Perez", nombre = "Tobías", edad = 34)
#Otro ejemplo
def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

example_function(name='John', age=25, city='New York')

# Variables por defecto / Esto nos dará la posibilidad de NO enviar ese argumento (opcional)

def decir_pais(pais = "Argentina"): #ESTO SIGNIFICA QUE SI NO LE PASAS NINGUN ARGUMENTO POR DEFECTO PONDRA "ARGENTINA"
    print(f"El nombre de mi país es {pais}")

decir_pais("México")
decir_pais()

# Retornar valores

def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def multiplicacion(a,b):
    return a * b
def division(a,b):
    return a // b

resultado_suma = suma(3,2)
resultado_resta = resta(5,3)
resultado_multiplicacion = multiplicacion(5,5)
resultado_division = division(10,2)

print(resultado_suma)
print(resultado_resta)
print(resultado_multiplicacion)
print(resultado_division)


# Otros tipos de datos que podríamos pasar:

lista = ['JavaScript', 'Python', True, 65]
number = 33

def usar_tipos_de_datos(lista, number): #LISTA Y NUMBER AUNQUE SE LLAMEN IGUAL NO SON LOS DE ARRIBA , ESTAS SON VARIABLES INTERNAS
    print(lista)
    print(number)

usar_tipos_de_datos(lista, number) # AQUI LO QUE PASA ESQUE COINCIDEN