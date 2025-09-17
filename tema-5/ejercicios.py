notas = {
    "Ana": 7.5,
    "Luis": 8.2,
    "Marta": 6.9,
    "Carlos": 9.1
}
nombres = input("Cual es tu nombre ")

if nombres in notas:
    print("la nota es:", notas[nombres])
else :
    print("Estudiante no encontrado")

#ejercicio 4
evento1 = {"Ana", "Luis", "Pedro", "Sofía"}
evento2 = {"Marta", "Luis", "Carlos", "Ana"}
fueron_al_evento = evento1 & evento2
print("fueron a los 2 evento : " , fueron_al_evento)

# ejercicio final 
# sistema de menu con precios 
# Menú usando diccionario
menu = {
    "Pizza": 8.50,
    "Hamburguesa": 6.00,
    "Ensalada": 5.00,
    "Pasta": 7.50,
    "Sopa": 4.00
}

# Pedido del cliente (usamos set para evitar duplicados)
pedido = set()

print("=== Bienvenido al restaurante ===")
print("Menú disponible:")
for plato, precio in menu.items():
    print(f"{plato}: ${precio}")

while True:
    opcion = input("\nEscribe el nombre del plato que quieres (o 'salir' para terminar): ").title()
    
    if opcion == "Salir":
        break
    
    if opcion in menu:  # verificamos que esté en el menú
        pedido.add(opcion)
        print(f"✅ {opcion} agregado al pedido.")
    else:
        print("❌ Ese plato no está en el menú.")

# Calcular el total
total = sum(menu[plato] for plato in pedido)

print("\n=== Resumen del pedido ===")
for plato in pedido:
    print(f"- {plato}: ${menu[plato]}")
print(f"\n💰 Total a pagar: ${total}")
