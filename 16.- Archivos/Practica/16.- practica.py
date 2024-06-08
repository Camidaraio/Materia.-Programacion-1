"""
1. Crear una función que reciba como parámetros una lista de
números y el path de un archivo. La misma deberá guardar la lista
en un archivo de texto."""

def archivos_con_numeros(lista_numeros, nombre_archivos):
    """"""
    with open(nombre_archivos, "w") as archivo_numeros:
        for numeros in lista_numeros:
            archivo_numeros.write(f"{numeros}\n")

    

lista_numeros = [2,4,6,8,10,15, 3, 5]
archivo_numeros = "archivo_numeros.txt"

archivos_con_numeros(lista_numeros, archivo_numeros)


"""
2. Crear una función que reciba como parámetro el path de un
archivo. La misma deberá leer el archivo del ejercicio anterior, solo
dejando pasar a la lista los números múltiplos de 2.
"""


def leer_archivos(archivo):
    """"""
    lista_numeros = []
    with open(archivo, "r") as archivo_numeros:
        for numero in archivo_numeros:
            numero = numero.strip()
            if numero.isdigit():
                    numero = int(numero)
                    if numero % 2 == 0:
                        lista_numeros.append(numero)
                
    return lista_numeros

archivo_path = archivo_numeros
numeros_multiplos_de_2 = leer_archivos(archivo_path)
print(numeros_multiplos_de_2)

"""
3. Crear una función que reciba como parámetros dos paths: uno
correspondiente a un archivo de origen y otro correspondiente a
un archivo de destino. La función debe leer el contenido del
archivo de origen y luego transcribirlo en el archivo de destino. En
caso de error la función retornará algún tipo de código de error
indicando que paso.
"""

def copiar_archivo(archivo_origen, archivo_destino):
    """"""
    
"""
4. Crear una función llamada contar_elementos que recibe como
parámetro el path de un archivo de texto que contiene un poema.
La función deberá contar la cantidad de líneas, la cantidad de
palabras y la cantidad de caracteres que contiene el poema. La
función retornará un diccionario con los datos obtenidos.
"""