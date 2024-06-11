from funciones import *

import csv

def leer_csv_como_diccionarios(nombre_archivo):
    """Lee un archivo CSV y lo convierte en una lista de diccionarios."""
    lista_diccionarios = []
    with open(nombre_archivo, 'r', newline='', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            lista_diccionarios.append(fila)
    return lista_diccionarios

# Llamada a la función
nombre_archivo = '17.- PARCIAL/Proyectos.csv'
lista_proyectos = leer_csv_como_diccionarios(nombre_archivo)

# Imprimir la lista de diccionarios
for proyecto in lista_proyectos:
    print(proyecto)

#lista_empleados = []

# archivo = open("17.- PARCIAL/Proyectos.csv", "r")
# lector_csv = archivo.read()
# for fila in lector_csv:
#     lista_empleados.append(fila)

# for empleado in lista_empleados:
#     print(empleado)
# archivo.close()

while True:
    print("""1.- Ingresar proyecto \n2.- Modificar proyecto: \n3.- Cancelar proyecto \n4.- Comprobar proyectoss \n5.- Mostrar todos \n6.- Calcular presupuesto promedio \n7.- Buscar proyecto por nombre \n8.- Ordenar proyectos \n9.- Retomar proyecto: \n10.- Salir""")
    

    opcion = pedir_entero("Ingrese un valor: ", "ERROR, ingrese una opcion correcta", 1, 10)

    match opcion:
        case 1:
            #ID A DEFINIR
            nombre_del_proyecto = pedir_str("ingrese el nombre: ", "nombre invalido")
            descripcion = pedir_str("ingrese el apellido: ", "apellido invalido")
            inicio_del_proyecto = solicitar_fechas()
            finalizacion_del_proyecto = solicitar_fechas()
            presupuesto = pedir_str("Ingrese su estado actual ACTIVO||INACTIVO: ", "Ingrese un dato valido")
            Estado = pedir_str("Ingrese su estado actual ACTIVO||FINALIZADO||CANCELADO: ", "Ingrese un dato valido")

            agregar_alumno(nombre_del_proyecto, descripcion, inicio_del_proyecto, finalizacion_del_proyecto, presupuesto, Estado)
            print("Alumno agregado")
        case 2:
            pass
        case 3:
            pass
        case 4: 
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass
        case 9:
            pass
        case 10:
            print("Saliendo...")
            break