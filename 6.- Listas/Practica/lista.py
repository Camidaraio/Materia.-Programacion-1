#Alumno: Camila Daraio. 
#Falta entregar


#Ejercicios:

"""
1.Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el
promedio de todos los números
"""
lista_enteros = [5, 5, 0, -6]

def calcular_promedio(lista):
    """"""
    suma = 0



    for i in range(len(lista)):
        suma += i
    contador = len(lista) 
    promedio = suma / contador
    return promedio




"""
2. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el
promedio de los números positivos

"""



def calcular_promedio_positivos(lista):
    """ 
    Calcula el promedio unicamente de numeros positivos de una lista
    """
    suma = 0
    promedio = 0 
    contador = 0
    for i in (lista):
        if i > 0:  
            suma += i
            contador += 1


    promedio = suma / contador
    return promedio


#print(calcular_promedio_positivos(lista_enteros))


"""
3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista
que recibe como parámetro.
"""

def listasss(lista):
    """"""
    for i in range(len(lista)):
        print(lista[i])
    
#listasss(lista_enteros)


"""
4. Escribir una función que reciba como parámetros una lista de enteros y retorne la posición
del valor máximo encontrado.
"""

def maximo(lista):
    """ 
    Encuentra el maximo dentro de una lista de enteros
    """
    maximo = None
    for i in range(len(lista)):
        if maximo == None or lista[i] > maximo:
            maximo = lista[i]
    return maximo

print(maximo(lista_enteros))