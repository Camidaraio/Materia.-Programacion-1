from funciones_AMB import *

lista_alumnos =[{"Nombre": "Pepito", "Apellido":"Perez", "Legajo":10, "Nota_final":5, "Estado": "ACTIVO"},
                {"Nombre":"Juan", "Apellido":"Perez", "Legajo":20, "Nota_final":4, "Estado": "ACTIVO"}]

#ALTA BAJA Y MODIFICACION

while True:
    print("""1.- Listar alumnos \n2.- Agregar alumnos \n3.- Modificar alumnos \n4.- Baja alumnos \n5.- Salir""")
    

    opcion = pedir_entero("Ingrese un valor: ", "ERROR, ingrese un valor correcto", 1, 5)

    match opcion:
        case 1:
            listar_alumnos(lista_alumnos)
        case 2:
            nombre_ingresado = pedir_str("ingrese el nombre: ", "nombre invalido")
            apellido_ingresado = pedir_str("ingrese el apellido: ", "apellido invalido")
            legajo_ingresado = pedir_entero("ingrese el legajo: ", "ERROR, ingrese un valor correcto", 0, 100)
            nota_ingresada = pedir_entero("ingrese la nota final: ", "ERROR, ingrese un valor correcto", 1, 10)
            estado_ingresado = pedir_str("Ingrese su estado actual ACTIVO||INACTIVO: ", "Ingrese un dato valido")

            agregar_alumno(nombre_ingresado, apellido_ingresado, legajo_ingresado, nota_ingresada, estado_ingresado, lista_alumnos)
            print("Alumno agregado")
        case 3:
            legajo_ingresado = pedir_entero("Ingrese el legajo del alumno a modificar", "ERROR, el legajo ingresado no existe", 1, 100)

            print("--------------")
            mostrar_claves(lista_alumnos[0])
            print("--------------")

        case 4: 
            pass
        case 5:
            print("Saliendo...")
            break
