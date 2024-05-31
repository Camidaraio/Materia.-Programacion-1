#Alumno: Camila Daraio. 
#Falta entregar


#Ejercicios:

"""
1.Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el
promedio de todos los números
"""
lista_enteros = [300, 5, 2, 0, -6, 10]

def calcular_promedio(lista):
    """"""
    acumulador = 0
    for i in range(len(lista)):
        acumulador += lista[i]
   
    promedio = acumulador / len(lista) 
    return promedio




"""
2. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el
promedio de los números positivos

"""



def calcular_promedio_positivos(lista):
    """ 
    Calcula el promedio unicamente de numeros positivos de una lista
    """

    for i in (lista):
        if i > 0:  
          promedio = calcular_promedio(lista)  
 
    return promedio


#print(calcular_promedio_positivos(lista_enteros))


"""
3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista
que recibe como parámetro.
"""

def calcular_producto(lista):
    """"""
    acumulador = 1

    for i in range(len(lista)):
        acumulador *= lista[i]
    
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

#print(maximo(lista_enteros))

"""
5. Escribir una función que reciba como parámetros una lista de enteros y muestre la/las
posiciones en donde se encuentra el valor máximo hallado."""

def posicion_maximo(lista):
    """"""
    """ 
    Encuentra el maximo dentro de una lista de enteros
    """
    maximo = None
    for i in range(len(lista)):
        if maximo == None or lista[i] > maximo:
            maximo = lista[i]
            

    return maximo

print(posicion_maximo(lista_enteros))



""""
6. Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista
de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe
reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente
reemplazo y luego retornar la cantidad total de reemplazos realizados.
"""

def reemplazar_nombres(lista_nombres, nombre_a_reemplazar, nuevo_nombre):
    """"""
