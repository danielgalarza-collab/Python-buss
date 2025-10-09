#La Programación Orientada a Objetos es un paradigma de programación que organiza el código en objetos, los cuales combinan datos (atributos) y funciones (métodos) que operan sobre esos datos.

#Los objetos son instancias de clases 
# Las clases son una plantilla para crear objetos  

#ejemplo 
class Perro:
    pass  # Por ahora no hace nada

mi_perro = Perro()  # Creamos un objeto de la clase Perro

#Atributos
# Los atributos son variables que describen al objeto.
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo nombre
        self.edad = edad      # Atributo edad

mi_perro = Perro("Laika", 10)
print(mi_perro.nombre)  # Laika
print(mi_perro.edad)    # 10

# importante 
#__init__ es el constructor, se ejecuta al crear un objeto.
#self hace referencia al propio objeto.


#METODOS
# Los métodos son funciones dentro de la clase que definen el comportamiento del objeto.
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print(f"{self.nombre} está ladrando")

mi_perro = Perro("Laika", 10)
mi_perro.ladrar()  # Laika está ladrando

#Encapsulamiento
#Es la práctica de proteger los atributos para que no se modifiquen directamente desde fuera de la clase.
class Perro:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

mi_perro = Perro("Laika", 10)
print(mi_perro.get_nombre())  # Laika
mi_perro.set_nombre("Rex")
print(mi_perro.get_nombre())  # Rex

#Los atributos privados se nombran con __
#Usamos getters y setters para acceder/modificar.

#Herencia 
#La herencia permite que una clase herede atributos y métodos de otra clase.
class Animal:
    def __init__(self, especie):
        self.especie = especie

    def comer(self):
        print(f"El {self.especie} está comiendo")

class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__("Perro")  # Hereda especie
        self.nombre = nombre
        self.edad = edad

mi_perro = Perro("Laika", 10)
mi_perro.comer()  # El Perro está comiendo

#super() llama al constructor de la clase padre.

#Polimorfismo
#El polimorfismo permite que distintos objetos respondan de forma distinta al mismo método.
class Gato(Animal):
    def comer(self):
        print(f"El {self.especie} está comiendo pescado")

mi_gato = Gato("Gato")
mi_gato.comer()  # El Gato está comiendo pescado

# Aquí, comer() es el mismo método que en Animal, pero cada clase lo implementa distinto.


# RESUMEN 
'''
Clase : molde para crear objetos , ejemplo : class Perro:
Objeto : Instancia de una clase  , ej : mi_perro = Perro("Laika",10)
Atributo : Variable del Objeto , ejemplo: self.nombre
Metodo: Funcion del objeto , ejemplo : def ladrar(self)
Encapsulamiento : Ocultar Atributos Internos , ejemplos : _nombre + getters/setters
Herencia: Clase Hija obtiene atributos/ metodos de otra clase , ejemplo class Perro(Animal)
Polimorfismo : Mismo metodo, distinto comportamiento , ejemplo : comer() en gato  / animal 
'''