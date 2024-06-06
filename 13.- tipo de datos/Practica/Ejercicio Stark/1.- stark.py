
from data_stark import *


#Camila Daraio

def verificar_no_vacio(lista):
    """
    Verifica si una lista está vacia

    Parametros:
    - lista: La lista que se va a verificar

    Retorna:
    - bool: True si la lista está vacía, False en caso contrario
    """

    if not lista:
        print("Lista vacia")
        return False
    else:
        return True
def normalizar_datos(lista):
    """
    Normaliza los datos numericos en la lista de heroes.

    Parametros:
    - lista_personajes: Una lista de diccionarios que representan héroes, donde algunas claves contienen datos numericos.

    Retorna:
    - bool: True si se realizaron cambios en los datos, False en caso contrario

    """
    verificar_no_vacio(lista)

    cambios_realizados = False

    for heroe in lista:
        for clave, valor in heroe.items():
            if type(valor) == str and valor.replace(".", "").isdigit():
                cambios_realizados = True
                if "." in valor:
                    heroe[clave] = float(valor)
                else:
                    heroe[clave] = int(valor)

    if cambios_realizados == True:
        print("Se realizaron cambios en los datos")

    return cambios_realizados

#normalizar_datos(lista_personajes)

def obtener_dato(heroe, clave):
    """
    Obtiene el valor de una clave de un heroe

    Parametros:
    - diccionario: lista_heroes
    - clave: la clave del héroe

    Devuelve:
    - El valor de la clave
    """ 
    retorno = False

    if len(heroe) > 0 and clave in heroe:
        retorno = heroe[clave]
    return retorno

#print(obtener_dato(lista_personajes[0], "nombre"))

def obtener_nombre(heroe):
    """
    
    """
    nombre = obtener_dato(heroe, "nombre")
    if nombre == False:
        retorno = False
    else:
        retorno =  f"Nombre: {nombre}"
    return retorno


#print(obtener_nombre(lista_personajes))

def obtener_nombre_y_dato(heroe,clave):
    """"""
    if len(heroe) > 0:
        nombre = obtener_nombre(heroe)
        dato = obtener_dato(heroe, clave)
        retorno = f"{nombre} | {clave}: {dato}"
    else:
        retorno = False
    return retorno

def obtener_maximo(lista, clave):
    retorno = False
    if len(lista) > 0:
        if type(lista[0][clave] == int or lista[0][clave] == float):
            for i in range(len(lista)):
                if i == 0 or maximo < lista[i][clave]:
                    maximo = lista[i][clave]
                retorno = maximo
    return retorno

# normalizar_datos(lista_personajes)
# print(obtener_maximo(lista_personajes, "fuerza"))


def obtener_minimo(lista, clave):
    retorno = False
    if len(lista) > 0:
        if type(lista[0][clave] == int or lista[0][clave] == float):
            for i in range(len(lista)):
                    if i == 0 or minimo > lista[i][clave]:
                        minimo = lista[i][clave]
                    retorno = minimo
    return retorno

# normalizar_datos(lista_personajes)
# print(obtener_minimo(lista_personajes, "fuerza"))

def obtener_dato_cantidad(lista_heroe,numero,key):
    lista = []
    for i in range(len(lista_heroe)):
        if lista_heroe[i][key] == numero:
            lista.append(lista_heroe[i])
    return lista

#print(obtener_dato_cantidad(lista_personajes,55,"fuerza"))


def stark_imprimir_heroes(lista_heroes):
    retorno = False
    mensaje = ""
    if len(lista_heroes) > 0:
        for i in range(len(lista_heroes)):
            for key,value in lista_heroes[i].items():
                mensaje += f"|| {key} : {value}\n"
        print(mensaje)
    else:
        return retorno

#stark_imprimir_heroes(lista_personajes)
    
def sumar_dato_heroe(lista_heroes,key):
    acumulador = 0
    if len(lista_heroes) > 0:
        if type(lista_heroes[0][key]) == int or type(lista_heroes[0][key]) == float:
            for i in range(len(lista_heroes)):
                if len(lista_heroes[i].keys()) > 0:
                    acumulador += lista_heroes[i][key]
    return acumulador
        
#print(sumar_dato_heroe(lista_personajes,"fuerza"))

def dividir(dividendo, divisor):
    if divisor == 0:
        retorno = False
    else:
        retorno = dividendo/divisor
    return retorno

#print(dividir(10,1000))

def calcular_promedio(lista_heroes,key):
    if type(lista_heroes[0][key]) == int or type(lista_heroes[0][key]) == float:
        dividendo = sumar_dato_heroe(lista_heroes,key)
        divisor = len(lista_heroes)
        promedio = dividir(dividendo,divisor)
        return promedio
# normalizar_datos(lista_personajes)   
# print(calcular_promedio(lista_personajes,"fuerza"))
        

def mostrar_promedio_dato(lista_heroes,key):
    if not lista_heroes:
        return False
    if type(lista_heroes[0][key]) == int or type(lista_heroes[0][key]) == float:
        promedio = calcular_promedio(lista_heroes, key)
        return promedio

# normalizar_datos(lista_personajes)
# print(mostrar_promedio_dato(lista_personajes,"altura"))

def imprimir_menu():
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

def validar_entero(valor : str):
    """
    Verifica si un string de numero está conformado unicamente por digitos

    Parametros:
    - valor: El string que se va a verificar

    Retorna:
    - True si el string está conformado unicamente por digitos, False en caso contrario

    """
    if valor.isdigit():
        return True
    else:
        return False
    
# print(validar_entero("4"))

def pedir_entero(mensaje, mensaje_error, minimo, maximo):
    """
    Validacion de la opcion ingresada
    """
    entero_ingresado = int(input(mensaje))
    while entero_ingresado < minimo or entero_ingresado > maximo:
        entero_ingresado = int(input(mensaje_error))
    return entero_ingresado


def stark_menu_principal():
    """"""
    imprimir_menu()
    while True:
        opcion = input("Debe ingresar un numero del 1 al 10: ")
        



def stark_marvel_app():
    pass

stark_menu_principal()