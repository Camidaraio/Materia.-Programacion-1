from funciones import *


lista_empleados = []

archivo = open("17.- Modelo parcial/Empleados.csv", "r")
lector_csv = archivo.read()
for fila in lector_csv:
    lista_empleados.append(fila)

for empleado in lista_empleados:
    print(empleado)
archivo.close()

while True:
    print("""1.- Ingresar empleados \n2.- Modificar empleados \n3.- Eliminar empleado \n4.- Mostrar todos \n4.- Calcular salario promedio \n4.- Buscar empleado por DNI \n4.- Ordenar empleados \n5.- Salir""")
    

    opcion = pedir_entero("Ingrese un valor: ", "ERROR, ingrese un valor correcto", 1, 8)

    match opcion:
        case 1:
            pass
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
            print("Saliendo...")
            break