from itertools import combinations
import random

print("Adivina Mi numero del 1 al 10")
numeros = input("escoje un numero del 1 al 10 : ")
if numeros == "5":  # ESTE ES EL NUMERO SECRETO
    print("Enhorabuena acertaste")
if numeros != 5:
    print("has fallado bro")
print("se termina el juego")

print("VAYAMOS A LA SEGUNDA PARTE DEL JUEGO ")
numero_elejido=input("elije un numero del 1 al 100 : ")
numero_ganador=random.randint (0, 100)
if numero_elejido == numero_ganador:
        print("Ganaste chabal")
if numero_elejido != numero_ganador:
        print("fallaste bro")
print("el numero ganador era {}" .format(numero_ganador))

# parte 2
class Solution:
    def convert_to_units(self, number: int):
        
        #Convertir un número en una lista de sus dígitos al revés.
        #123 -> [3, 2, 1]
        number_list = []  # lista vacía
        for d in str(abs(number)):  # usamos abs() para ignorar el signo
            number_list.insert(0, int(d))  # insertamos al inicio para invertir el orden
        return number_list

    def reverseNumber(self, num: int) -> int:
        
        #devolver el número invertido.
        #123 -> 321
        
        digits = self.convert_to_units(num)       # obtenemos los dígitos invertidos
        reversed_num = int("".join(map(str, digits)))  # reconstruimos el número desde la lista
        
        if num < 0:  # si era negativo, devolvemos el número con signo negativo
            reversed_num = -reversed_num
        
        
        return reversed_num

sol = Solution()
print(sol.reverseNumber(123))   #  321
print(sol.reverseNumber(-456))  #  -654
print(sol.reverseNumber(120))   #  21

#parte 3 : comprobar si un numero es palíndromo
num = 121 
num_str = str(num) # con esto pasamos el numero a formato string

reverso = num_str[::-1]

if num_str == reverso:
     print("Es palindromo")
else:
     print("No es palindromo")

#contar vocales en una palabra o frase 
class Solution:
    def contar_vocales(self, texto: str) -> int:
        texto = texto.lower()
        vocales = "aeiou"
        contador = 0

        for letra in texto:
            if letra in vocales:
                contador += 1

        return contador

sol = Solution()
print(sol.contar_vocales("Hola Mundo")) 
print(sol.contar_vocales("Python"))

#contar consonantes 
class Solution2 :
     def contar_consonantes(self, texto: str) -> int:
        texto = texto.lower()
        vocales = "aeiou"
        contador = 0

        for letra in texto:
            #aqui basicamente le decismo que si solo es una letra y esa letra no esta en vocales , aumenta el contador 
            if letra.isalpha() and letra not in vocales: # .isalpha() comprueba que la letra sea solo una letra , ni espacio ni numero ni simbolos
                 contador += 1
        
        return contador

Solucion = Solution2()
print(Solucion.contar_consonantes("Daniel"))

#ejercicio cuentas y banco 
class CuentaBancaria:
    def __init__(self, nombre):
        # 1. Guardar el nombre y saldo inicial en self
        self.nombre = nombre
        self.saldo = 0

    def depositar(self, cantidad):
        # 2. Sumar cantidad al saldo
        self.saldo += cantidad

    def retirar(self, cantidad):
        # 3. Restar cantidad si hay suficiente dinero
        if self.saldo >= cantidad:
            self.saldo - cantidad
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        # 4. Imprimir saldo de esta cuenta
        print(f"Cuenta {self.nombre}: saldo = {self.saldo}")


# Crear dos cuentas
cuenta1 = CuentaBancaria("Ana")
cuenta2 = CuentaBancaria("Luis")

# Depositar y retirar dinero
cuenta1.depositar(100)
cuenta1.retirar(30)
cuenta1.mostrar_saldo()  #  deberia mostrar 70

cuenta2.depositar(200)
cuenta2.retirar(250)     #  deberia decir "Saldo insuficiente"
cuenta2.mostrar_saldo()  #  deberia mostrar 200
