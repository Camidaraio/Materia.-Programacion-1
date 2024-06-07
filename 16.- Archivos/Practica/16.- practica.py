def archivos_con_numeros(lista_numeros, nombre_archivos):
    """"""
    with open(nombre_archivos, "w") as archivo_numeros:
        for numeros in lista_numeros:
            archivo_numeros.write(f"{numeros}")

lista_numeros = [1,2,3,4]
archivo_numeros = "archivo_numeros.txt"

archivos_con_numeros(lista_numeros, archivo_numeros)




