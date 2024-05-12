#Alumno: Camila Daraio. 
#Falta entregar


#Ejercicios:

"""
1.Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el
promedio de todos los números
"""

suma = 0

lista_enteros = [5,5]

for i in range(len(lista_enteros)):
    suma += i
contador = len(lista_enteros) 
promedio = suma / contador



"""
2. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el
promedio de los números positivos
"""

suma = 0
promedio = 0 

lista_enteros = [5, 5, 0, -6]

for i in (lista_enteros):
    if i > 0:  
        suma += i
        contador += 1


promedio = suma / contador
print(promedio)


"""
3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista
que recibe como parámetro.
"""


"""
4. Escribir una función que reciba como parámetros una lista de enteros y retorne la posición
del valor máximo encontrado.
"""

