from funciones import *


lista_empleados = []

archivo = open("17.- PARCIAL/Proyectos.csv", "r")
lector_csv = archivo.read()
for fila in lector_csv:
    lista_empleados.append(fila)

for empleado in lista_empleados:
    print(empleado)
archivo.close()

while True:
    print("""1.- Ingresar proyecto: \n2.- Modificar proyecto: \n3.- Cancelar proyecto \n4.- Comprobar proyectos: \n5.- Mostrar todos \n6.- Calcular presupuesto promedio \n7.- Buscar proyecto por nombre \n8.- Ordenar proyectos \n9.- Retomar proyecto: \n10.- Salir""")
    

    opcion = pedir_entero("Ingrese un valor: ", "ERROR, ingrese una opcion correcta", 1, 10)

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
            pass
        case 9:
            pass
        case 10:
            print("Saliendo...")
            break