from stark import * 

def imprimir_menu2():
    """
    Imprime un menu
    """
    print("Eliga una opcion: \n",
        "1- Normalizar datos \n ",
        "2- Imprimir nombres de NB: \n ",
        "3- superhéroe mas alto del genero F: \n ",
        "4- superhéroe mas alto del genero M: \n ",
        "5- superhéroe mas debil del genero M: \n ",
        "6- superhéroe mas debil del genero NB: \n ",
        "7- fuerza promedio de los superhéroes de género NB: \n ",
        "8- cuántos superhéroes tienen cada tipo de color de ojos: \n,",
        "9- cuántos superhéroes tienen cada tipo de color de pelo: \n",
        "10- todos los superhéroes agrupados por color de ojos: \n",
        "11- todos los superhéroes agrupados por tipo de inteligencia: \n",
        "12- Salir: \n ",
        )
    
def stark_menu_principal2():
    """"""
    imprimir_menu2()
    while True:
        opcion = input("Debe ingresar un numero del 1 al 12: ")
        if validar_entero(opcion):
            opcion = int(opcion)
            if opcion < 1 or opcion > 12:
                print("opcion incorrecta")
            else:
                return opcion
        else:
            print("ingrese un numero valido")

def stark_marvel_app2():
    """
    Funcion principal de la aplicación Stark Marvel

    Parametros:
    - lista_heroes: Una lista de diccionarios que representan cada heroe.
    """
    acceso_permitido = False

    while True:
        opcion = stark_menu_principal2()
        if opcion == 1:
            acceso_permitido = normalizar_datos(lista_personajes)
        if acceso_permitido:
            if opcion == 2:
                heroes_NB = []
                for heroe in lista_personajes:
                    if heroe["genero"]  == "NB":
                        heroes_NB.append(heroe["nombre"])

                for heroes in heroes_NB:
                    print(heroes)

            elif opcion == 3:
                mas_alto = obtener_maximo(lista_personajes, "altura")

                for heroe in lista_personajes:
                    if heroe["genero"]  == "F":
                        mas_alto_F_nombre = heroe["nombre"]
                print(mas_alto_F_nombre)

            elif opcion ==  4:
                mas_alto = obtener_maximo(lista_personajes, "altura")
                for heroe in lista_personajes:
                    if heroe["genero"]  == "M":
                        mas_alto_F = heroe["nombre"]
                print(mas_alto_F)
            elif opcion ==  5:
                print(obtener_maximo(lista_personajes, "fuerza"))
            elif opcion ==  6:
                print(obtener_minimo(lista_personajes, "fuerza"))
            elif opcion ==  7:
                print(obtener_dato_cantidad(lista_personajes,55,"fuerza"))
            elif opcion ==  8:
                stark_imprimir_heroes(lista_personajes)
            elif opcion ==  9:
                print(sumar_dato_heroe(lista_personajes,"fuerza"))
            elif opcion == 10:
                print(dividir(10,1000))
            elif opcion == 11:
                print(calcular_promedio(lista_personajes,"fuerza"))
            elif opcion ==  12:
                print(mostrar_promedio_dato(lista_personajes,"altura"))
            elif opcion == 13:
                print(validar_entero("4"))
            elif opcion == 13:
                print("Saliendo...")
                break
        else:
            print("Primero debes seleccionar la opción 1.")


    
stark_marvel_app2()
