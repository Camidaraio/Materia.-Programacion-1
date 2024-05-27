
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
        print("Se realizaron cambios en los datos \n")

    return cambios_realizados


def obtener_dato(lista_heroes, clave):
    """
    Obtiene el valor de una clave de un heroe

    Parametros:
    - diccionario: lista_heroes
    - clave: la clave del héroe

    Devuelve:
    - El valor de la clave
    """ 


def obtener_nombre(lista_heroes):
    """
    
    """

    