'''
Listas simples:
1- Realizar una función que ordene una lista de entero en orden ascendente o
descendente dependiendo de un parámetro que se le envíe, la función debe retornar
la cantidad de cambios que se realizaron.'''



lista_enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def ordemiento_ascendentes_descendente(lista_enteros, orden= True):
    contador = 0
    for i in range(len(lista_enteros)):
        for j in range(i+1,len(lista_enteros),1):
            if orden == True:
                if(lista_enteros[i] < lista_enteros[j]):
                    aux = lista_enteros[i]
                    lista_enteros[i] = lista_enteros[j]
                    lista_enteros[j] = aux
                    contador += 1 
            else:
                if(lista_enteros[i] > lista_enteros[j]):
                    aux = lista_enteros[i]
                    lista_enteros[i] = lista_enteros[j]
                    lista_enteros[j] = aux
                    contador += 1 

    return contador


print(ordemiento_ascendentes_descendente(lista_enteros, True))
print(lista_enteros)

'''
2- Realizar una función que ordene una lista de nombres de la A-Z o viceversa
dependiendo de un parámetro que se le envíe, la función debe retornar la cantidad
de cambios que se realizaron.'''

lista_nombres = ["Juan", "Maria", "Luis", "Ana", "Carlos", "Fernanda", "Santiago", "Teresa", "oscar", "Benjamin", "Karla", "Hector", "Veronica", "Gabriel", "Natalia", "Isabel", "Wilson", "Rosa", "Daniela", "Esteban", "Yolanda", "Zoila", "Ximena", "Patricia", "ursula", "Quirino"]

def ordemiento_nombres(lista_nombres, orden = True):

    contador = 0
    for i in range(len(lista_nombres)):
        for j in range(i+1,len(lista_nombres),1):
            if orden == True:
                if(lista_nombres[i][0] < lista_nombres[j][0]):
                    aux = lista_nombres[i]
                    lista_nombres[i] = lista_nombres[j]
                    lista_nombres[j] = aux
                    contador += 1 
            else:
                if(lista_nombres[i][0] > lista_nombres[j][0]):
                    aux = lista_nombres[i]
                    lista_nombres[i] = lista_nombres[j]
                    lista_nombres[j] = aux
                    contador += 1 

    return contador

print(ordemiento_nombres(lista_nombres, False))
print(lista_nombres)


'''
3- Similar a la función anterior, se debe realizar otra que ordene una lista de
nombres por su largo, de manera ascendente o descendente, la función debe
retornar la cantidad de cambios que se realizaron'''
def ordenar_lista_nombres_ascendente_descendente_por_largo(lista : list, orden = True):
    contador = 0
    for i in range(len(lista)):
        for j in range(i+1,len(lista),1):
            if(orden == True):
                if(len(lista[i]) > len(lista[j])):
                    auxiliar = lista[i]
                    lista[i] = lista[j]
                    lista[j] = auxiliar
                    contador += 1 
            else:        
                if(len(lista[i]) < len(lista[j])):
                    auxiliar = lista[i]
                    lista[i] = lista[j]
                    lista[j] = auxiliar
                    contador += 1 
    return contador

print(lista_nombres)

print(ordenar_lista_nombres_ascendente_descendente_por_largo(lista_nombres,True))

print(lista_nombres)

'''
4- Ordenar una matriz de nombre-apellido de la A-Z o viceversa dependiendo de un
parámetro que se le envíe, por otro lado, la función deberá recibir otro parámetro
para indicar si la prioridad de ordenamiento la tendrá el nombre o el apellido.'''


matriz = [
    ["Maria", "Gonzales"],
    ["Luis", "Sanchez"],
    ["Ana", "Martinez"],
    ["Pedro", "Gomez"],
    ["Laura", "Dias"],
    ["Carlos", "Rodriguez"],
    ["Marta", "Lopez"],
    ["Diego", "Hernandez"],
    ["Eleno", "Moreno"]
]