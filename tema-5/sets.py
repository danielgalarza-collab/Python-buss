#Un set es una colección de elementos sin orden y sin elementos repetidos.

# Características clave:
#No tiene índices (no podés hacer set[0])

#No permite duplicados , ADEMAS LOS SETS SE CREAN CON {}

#Muy útil para operaciones de conjuntos: unión, intersección, diferencia

#🧪 Ejemplo rápido:

mi_set = {1, 2, 3, 3, 4}
print(mi_set)  # Resultado: {1, 2, 3, 4}
#➡️ El número 3 se repite, pero el set lo guarda una sola vez.
#¿Para qué se usan?
#Cosas muy específicas como:

#Eliminar duplicados de una lista

#Ver qué elementos tienen en común dos colecciones

#Operaciones matemáticas entre conjuntos (pero eso es poco común en backend)
#Resumen express para que no se te olvide:
#Set = como una lista, pero sin elementos repetidos y sin orden.
#No se accede por índice, y no se usa mucho en backend.