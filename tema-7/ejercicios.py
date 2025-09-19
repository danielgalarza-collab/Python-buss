import random
import string
# generador de password

def Generator_password(length, level=3):
    letras = string.ascii_letters
    numeros = string.digits

    simbolos = "!@#$%&*"

    if level == 1:
        contraseña = letras
    elif level == 2:
        contraseña = letras + numeros
    elif level == 3:
        contraseña = letras + numeros + simbolos
    else:
        raise ValueError("tienes que elejir un nivel entre el 1 , 2 y 3 ")
    
    password = "".join(random.choice(contraseña) for _ in range(length))
    return password

print(Generator_password(10, 1))  # solo letras
print(Generator_password(10, 2))  # letras + números
print(Generator_password(10, 3))  # letras + números + símbolos