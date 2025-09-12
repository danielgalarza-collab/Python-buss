####### NUMBERS

# int (Integer): Número entero
numero_entero = 10

# float: Número decimal
numero_decimal = 5.75 # AL PASARLO A INT NO REDONDEA , SOLO LE QUITA LA PARTE DECIMAL

# complex: numero complejo (parte entera y otra parte imaginaria)
numero_complejo = 5 + 2j

print(numero_entero)
print(type(numero_entero))      # ESTO NOS IMPRIME EL TIPO DE NUMERO QUE ES 

print(numero_decimal)
print(type(numero_decimal))
###### CASTEO

decimal_desde_entero = float(numero_entero)
entero_desde_decimal = int(numero_decimal)
complejo_desde_entero = complex(numero_entero)
complejo_desde_decimal = complex(numero_decimal)

print(decimal_desde_entero)
print(entero_desde_decimal)
print(complejo_desde_entero)
print(complejo_desde_decimal)

import random  # noqa: E402

aleatorio = random.randrange(1,10) # ESTO DA UN NUMERO ALEATORIO DEL 1 AL 10 , El número FINAL no es incluyente 
aleatorio_par = random.randrange(2,11,2) # Número par del 2 al 10 (incluído) EL TERCER DIGITO SIGNIFICA QUE TRABAJA CADA 2 NUMEROS , 
aleatorio_impar = random.randrange(1,10,2) #Número impar del 1 al 9 (incluído)

print(aleatorio)
print(aleatorio_par)
print(aleatorio_impar)