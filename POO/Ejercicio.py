class CuentaBancaria :
    def __init__(self,titular, saldo = 0):
        self.titular = titular 
        self.saldo = saldo
    
    def depositar(self,cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"se depositaron {cantidad}$ . Nuevo saldo : {self.saldo}$")
            
        else:
            print(" la cantidad a depositar debe ser positiva")
        
    def retirar(self, cantidad):
        if cantidad > self.saldo:
                print("Saldo insuficiente para realizar el retiro")
        elif cantidad <= 0:
                print("la cantidad a retirar debe ser positiva")
        else:
            self.saldo -= cantidad
            print(f"se retiraron {cantidad}$ . Nuevo saldo{self.saldo}$")
    
    def mostrar_saldo(self):
         print(f"saldo actual es de {self.titular}: {self.saldo}$")

mi_cuenta = CuentaBancaria("Daniel", 1000)
mi_cuenta.mostrar_saldo()  # Saldo actual de Daniel: 1000€
mi_cuenta.depositar(500)    # Se depositaron 500€. Nuevo saldo: 1500€
mi_cuenta.retirar(2000)     # Saldo insuficiente para realizar el retiro.
mi_cuenta.retirar(300)      # Se retiraron 300€. Nuevo saldo: 1200€
mi_cuenta.mostrar_saldo()   # Saldo actual de Daniel: 1200€



# ejercicio 2
# Clase base: Vehiculo 
class Vehiculo:
    # Constructor de la clase Vehiculo
    def __init__(self, marca, modelo):
        # Atributos básicos de cualquier vehículo
        self.marca = marca       # Marca del vehículo 
        self.modelo = modelo     # Modelo del vehículo 

    # Método general que indica que el vehículo se está moviendo
    def mover(self):
        print(f"El {self.marca} {self.modelo} se está moviendo.")

    # Método para mostrar información básica del vehículo
    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")


# Clase derivada 1: Coche
class Coche(Vehiculo):  # Hereda todo de Vehiculo
    # Constructor de la clase Coche
    def __init__(self, marca, modelo, combustible):
        # Llamamos al constructor de la clase base para asignar marca y modelo
        super().__init__(marca, modelo)
        self.combustible = combustible  # Cantidad de combustible en litros

    # Método mover sobrescrito (polimorfismo)
    def mover(self):
        if self.combustible > 0:  # Verificamos si hay combustible
            self.combustible -= 1  # Cada movimiento consume 1 litro
            print(f"El coche {self.marca} {self.modelo} está conduciendo. Combustible restante: {self.combustible}L")
        else:
            print(f"El coche {self.marca} {self.modelo} no puede moverse, se quedó sin combustible.")


#  Clase derivada 2: Bicicleta 
class Bicicleta(Vehiculo):  # Hereda de Vehiculo
    # Constructor de Bicicleta
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)  # Usamos constructor de la clase base
        self.tipo = tipo  # Tipo de bicicleta 

    # Método mover sobrescrito (polimorfismo)
    def mover(self):
        # La bicicleta no consume combustible, simplemente pedaleamos
        print(f"La bicicleta {self.marca} {self.modelo} ({self.tipo}) está pedaleando.")


#  Uso de las clases 
# Creamos una lista de vehículos de distintos tipos
vehiculos = [
    Coche("Toyota", "Corolla", 3),      # Coche con 3 litros de combustible
    Bicicleta("Trek", "Marlin 7", "montaña")  # Bicicleta de montaña
]

# Iteramos sobre la lista de vehículos
for v in vehiculos:
    v.mostrar_info()  # Mostramos información básica (marca y modelo)
    v.mover()         # Llamamos al método mover (polimorfismo hace que cada uno actúe distinto)
    print("---")       # Separador visual para entender mejor la salida
