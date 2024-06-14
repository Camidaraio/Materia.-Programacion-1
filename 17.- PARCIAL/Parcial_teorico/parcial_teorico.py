# lista = [78.5,2,6,88,7]

# for i in range(len(lista)):
#     if lista[i] > maximo:
#         maximo = lista[i]

# #print(maximo)


lista_alumnos = [{"nombre":"juan", "apellido":"Perez", "nota": 2},
                  {"nombre":"Maria", "apellido":"Gonzales", "nota": 4},
                  {"nombre":"jeremias", "apellido":"Gomez", "nota": 6},]

for i in range(len(lista_alumnos)):
    for clave,valor in lista_alumnos[i].items():
        mensaje = f"{clave}: {valor}"

    print(mensaje)