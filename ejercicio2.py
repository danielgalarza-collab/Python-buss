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