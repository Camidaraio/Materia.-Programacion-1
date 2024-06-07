#ARCHIVOS

# MODO DESCRIPCIÓN
# r Abre un archivo de texto sólo para lectura
# rb Abre un archivo binario sólo para lectura
# r+ Abre un archivo de texto para escritura y lectura
# w Abre un archivo de texto sólo para escritura (si existe lo sobreescribe)
# wb Abre un archivo binario sólo para escritura (si existe lo sobreescribe)
# w+ Abre un archivo de texto para escritura y lectura (si existe lo sobreescribe)
# a Abre un archivo para anexar información


#--------------------------------

#MODOS DE APERTURA

"""r -> abre un archivo sólo para lectura. El puntero al
archivo está localizado al comienzo del archivo.
Este es el modo predeterminado de la función."""

"""r+ -> abre un archivo para escritura y lectura. El
puntero del archivo está localizado al comienzo
del archivo."""

"""w -> abre un archivo solo para escritura.
Sobreescribe el archivo si este ya existe. Si el
archivo no existe lo crea."""
"""
w+ -> abre un archivo para escritura y lectura.
Sobreescribe el archivo si este ya existe. Si el
archivo no existe lo crea.
"""

"""a -> abre un archivo para anexo. El puntero del
archivo está al final del archivo si este existe. Es
decir, el archivo está en modo anexo. Si el archivo
no existe, crea un nuevo archivo para escritura.

EJEMPLO:

mensaje = Hola!!
file = open("datos.txt", "a")
file.write(mensaje)
file.close()
"""
# --------------------------------

#COMO ABRIR UN ARCHIVO EN PY:Para abrir un archivo con Python, podemos usar la función open.


"""
Abrir un archivo: open

archivo = open(nombre_archivo, modo)

archivo objeto file: el cual será utilizado para llamar a otros
métodos asociados con el archivo.

nombre_archivo: string que contiene el nombre del archivo
al que queremos acceder.

modo: string que contiene el modo de apertura del archivo.

Cerrar un archivo: close

archivo.close()

archivo objeto file que fue obtenido con el método open.
"""

#--------------------------

#MODOS

"""
archivo = open(nombre_archivo, modo)

archivo.closed: retorna True si el archivo está
cerrado, si no, False.

archivo.mode: retorna el modo de acceso con el que el
archivo se abrio.

archivo.name: retorna el nombre del archivo.

"""


#--------------------------

#EJEMPLO:

archivo_escritura = open("nombre_archivo.txt", "a")

archivo_escritura.write("Hola mundo")



#archivo_escritura.close()


#----------
"""Escribir un archivo en forma de lista.

Escribir: writelines


"""

#EJEMPLO
archivo = open('archivo.txt', 'w')
lineas_texto = ['Primer linea de texto\n',
'segunda linea\n',
'tercera linea\n']
archivo.writelines(lineas_texto)
archivo.close()

#-------------


"""Utilizando la función readline() es posible leer desde
la posición actual del puntero del archivo hasta el
final de la línea y luego posicionar el puntero al
comienzo de la siguiente línea.

Leer un archivo: readline
"""
archivo = open('archivo.txt', 'r+')
print(archivo.tell()) #Indica en que byte esta el puntero 0
linea = archivo.readline()
print(linea,end="") # Hola mundo
print(archivo.tell()) #Indica en que byte esta el puntero 11
# Cerramos el archivo
archivo.close()

#------------

"""El método seek permite modificar la posición
actual del puntero.

Mover puntero: seek
"""

# EJEMPLO:


archivo = open('archivo.txt', 'r+')
archivo.seek(11)
print(archivo.tell()) #Esta en el byte 11
linea = archivo.readline()
print(linea,end="") # Hola mundo
archivo.close()

#-----------------------------------------------------

"""
Podemos usar la sentencia with para abrir archivos en Python y dejar que el intérprete se
encargue de cerrar el mismo.

Administrador de contexto: with

with open('archivo.txt', 'r+') as archivo:
for linea in archivo:
print(linea, end="")

"""

#EXISTE OTRO TIPOS DE DOCUMENTOS
#CSV 
"""
El CSV es un tipo de documento que representa
los datos de forma parecida a una tabla, es decir,
organizando la información en filas y columnas.

Las columnas son separadas, por un signo de
puntuación (, ; .) u otro carácter y las diferentes
filas suelen separarse por un salto de línea.
"""

#JSON 
"""
El nombre es un acrónimo de las siglas en inglés de JavaScript Object Notation.
JSON es un formato para el intercambio de datos basado en texto. Por lo que es fácil de leer tanto
para una persona como para una máquina.
"""

#EJEMPLO

#JSON (Escritura)

"""
El paquete json permite traducir un diccionario a
formato JSON utilizando el método dump.
JSON (Escritura)
"""
import json

data = {}
data['clientes'] = []
data['clientes'].append({ 'nombre': 'Juan', 'edad': 27})
data['clientes'].append({ 'nombre': 'Ana', 'edad': 26})

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4, ensure_ascii=False )

#JSON (Lectura)
"""
La lectura es similar al proceso de escritura, se
debe abrir un archivo y procesar esté utilizando el
método load.
"""

import json

with open('data.json') as file:
    data = json.load(file)
