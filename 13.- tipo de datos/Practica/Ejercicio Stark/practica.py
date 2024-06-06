from data_stark import *


for clave in lista_personajes:
    nombre = clave["nombre"]
    print(nombre)

cceso_permitido = False

    while True:
        opcion = stark_menu_principal()
        if opcion == 1:
            acceso_permitido = normalizar_datos(lista_personajes)
        if opcion == 2:
            if acceso_permitido:
                print(obtener_dato(lista_personajes[0], "nombre"))
            else:
                print("Primero debes seleccionar la opción 1.")
        elif opcion == 3:
            if acceso_permitido:
                print(obtener_nombre(lista_personajes))
            else:
                print("Primero debes seleccionar la opción 1.")
        elif opcion ==  4:
            if acceso_permitido:
                print(obtener_nombre_y_dato(lista_personajes[1], "altura"))
            else:
                print("Primero debes seleccionar la opción 1.")
        elif opcion ==  5:
            if acceso_permitido:
                print(obtener_maximo(lista_personajes, "fuerza"))
            else:
                print("Primero debes seleccionar la opción 1.")
        elif opcion ==  6:
            if acceso_permitido:
                print(obtener_minimo(lista_personajes, "fuerza"))
        elif opcion ==  7:
            if acceso_permitido:
                print(obtener_dato_cantidad(lista_personajes,55,"fuerza"))
            else:
                print("Primero debes seleccionar la opción 1.")
        elif opcion ==  8:
            if acceso_permitido:
                stark_imprimir_heroes(lista_personajes)
            else:
                print("Primero debes seleccionar la opción 1.")
        elif opcion ==  9:
            if acceso_permitido:
                print(sumar_dato_heroe(lista_personajes,"fuerza"))
            else:
                print("Primero debes seleccionar la opción 1.")
        elif opcion == 10:
            if acceso_permitido:
                print(dividir(10,1000))
            else:
                print("Primero debes seleccionar la opción 1.")
        elif opcion == 11:
            if acceso_permitido:
                print(calcular_promedio(lista_personajes,"fuerza"))
            else:
                print("Primero debes seleccionar la opción 1.")
        elif opcion ==  12:
            if acceso_permitido:
                print(mostrar_promedio_dato(lista_personajes,"altura"))
            else:
                print("Primero debes seleccionar la opción 1.")
        elif opcion == 13:
            if acceso_permitido:
                print(validar_entero("4"))
            else:
                print("Primero debes seleccionar la opción 1.")
        elif opcion == 13:
            print("Saliendo...")
            break