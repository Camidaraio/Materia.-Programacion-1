#TIPOS DE DATPOS

"""
TUBLAS:
"""

"""
SET:
- 
- No son mutables
- No se pueden acceder a los elementos de un set
- Si se pueden agregar datos con el 'add'
"""
mi_set = {10,25,2,5,6,5}

mi_set.add("pepe")
mi_set.remove(5)

#print(mi_set)

"""

METODOS:

add: agrega un elemento
remove: elimina un elemento
discard: 
"""

#-------------------

"""
DICCIONARIO
- tiene clave y valor

"""
#EJEMPLO

diccionario = {"Nombre":"Luis", "Ciudad":"Buenos Aires", "Edad":"21"}

print(diccionario["Nombre"])

"""
metodo get:
accede a un valor de un diccionari

metodo keys:
te devuelve todas las claves

metodos values:
te devuelve todos los valores

metodo pop:
elimina el valor o la clase 
diccionario.pop("Nombre")
"""
diccionario.pop("Nombre")

print(diccionario["Nombre"])