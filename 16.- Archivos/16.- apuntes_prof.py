#archivo_escritura = open('archivo_prueba.txt','w')

# archivo_escritura.write('Hola mundo')
# archivo_escritura.write('\n Me llamo Luis')

#lista_a_escribir = ['Hola mundo','\n Me llamo Luis']

#archivo_escritura.writelines(lista_a_escribir)
#Este for equivale a esta funcion ^ 
# for i in range(len(lista_a_escribir)):
#     archivo_escritura.write(lista_a_escribir[i]+'\n')


#archivo_escritura.close()


archivo_lectura = open('archivo_prueba.txt','r')

#print(archivo_lectura)

#lectura = archivo_lectura.read(10) -> Lee solo 10 caracteres
#archivo_lectura.seek(0)
#print(archivo_lectura.tell())
#lectura = archivo_lectura.read(500) -> Lee hasta que se queda sin nada que leer (NO ROMPE)
#lectura_dos = archivo_lectura.read() -> Lee lo que falta del archivo (en caso de usarse primero, todo)

# print(lectura, end="")
# print(lectura_dos)

# for linea in archivo_lectura.readlines():
#   print(linea, end="")

# for linea in archivo_lectura:
#     print(linea, end="")

archivo_lectura.close()


# with open('archivo_prueba.txt', 'r+') as archivo:
#     for linea in archivo:
#         print(linea, end="")

# print(archivo.closed)


import json

# datos = {}

# datos['clientes'] = []
# datos['clientes'].append({ 'nombre': 'Juan', 'edad': 27})
# datos['clientes'].append({ 'nombre': 'Ana', 'edad': 26})

# with open('datos.json', 'w') as archivo_json:
#     json.dump(datos, archivo_json, indent=4, ensure_ascii=False)


archivo_json = open('datos.json','r')

datos = json.load(archivo_json)

archivo_json.close()

# Abrimos el archivo en modo LECTURA, obtenemos los datos y cerramos el archivo 

lista_datos = datos['clientes']
lista_datos[0]['nombre'] = 'Pedro'
datos['clientes'] = lista_datos

# Trabajamos con los datos DE MANERA LOCAL, modificamos lo que queremos pero
# NO HAY REPERCUCION EN EL ARCHIVO ORIGINAL

archivo_json = open('datos.json','w')

json.dump(datos,archivo_json, indent=4, ensure_ascii=False)

archivo_json.close()

# MODIFICAMOS el archivo ORIGINAL con los datos con los que trabajamos anteriormente