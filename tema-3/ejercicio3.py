# PARTE 1
palabra=input("Escribe una palabra : ")

print("la palabra tiene" , len(palabra) , "caracteres")
print("la primera letra de",(palabra) , "es", (palabra[0]))

#PARTE 2
palabra = input("Escribe una palabra: ")

cantidad = len(palabra)

primera = palabra[0]
ultima = palabra[-1]

print("La palabra tiene", cantidad, "letras.")
print("La primera letra es:", primera)
print("La última letra es:", ultima)

#PARTE 3  pig latin Translator
def pig_latin(palabra):
    vocales = "aeiou"   #definimos las vocales 
    if palabra[0].lower() in vocales:   #Comprobamos si la primera letra es una vocal
            return palabra + "yay" # Si empieza por vocal: devolvemos la palabra + "yay"
    else:
            return palabra[1:] + palabra [0] + "ay" # esta linea se ejecuta si la primera letra es consonante 

print(pig_latin("hello"))

print(pig_latin("Germany"))