lista_enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def ordemiento_numeros_ascendentes():
    for i in range(len(lista_enteros)):
        for j in range(i+1,len(lista_enteros),1):
            if(lista_enteros[i] < lista_enteros[j]):
                aux = lista_enteros[i]
                lista_enteros[i] = lista_enteros[j]
                lista_enteros[j] = aux

    return lista_enteros


print(ordemiento_numeros_ascendentes())

nombres = ["valentin","lautaro", "juan", "pedro", "pepito", "carla"]

def ordemiento_nombres():

    for i in range(len(nombres)):
        for j in range(i+1,len(nombres),1):
            if (nombres[i] < nombres[j]):
                aux = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux

    return nombres