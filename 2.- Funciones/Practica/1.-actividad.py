"""
CAMILA DARAIO

EJERCICIOS DE FUNCIONES

HACER UN MENU DE OPCIONES

# Ejercicio 01: Escribe una función que calcule el área de un círculo. La función debe recibir
# el radio como parámetro y devolver el área.

# Ejercicio 02: Crea una función que verifique si un número dado es par o impar. La función
# debe imprimir un mensaje indicando si el número es par o impar.

# Ejercicio 03: Define una función que encuentre el máximo de tres números. La función
# debe aceptar tres argumentos y devolver el número más grande.

# Ejercicio 04: Diseña una función que calcule la potencia de un número. La función debe
# recibir la base y el exponente como argumentos y devolver el resultado.

# Nota: Todas las funciones deben estar probadas y se podrá acceder a cada una de
# ellas mediante un menú de opciones.
"""

#EJERCICIO 1

def calcular_area_circulo(radio):
    """ 
        Que hace: sirve para calcular el area de un circulo
        Recibe: radio del circulo
        Devuelve: el radio del circulo
    
    """
    area = 3.14 * (radio **2)

    return area

#EJERCICIO 2

def par_impar(numero):
    """ Que hace: Determina si un numero es par o impar
        Recibe: un numero
        Devuelve: si es par o impar
    
    """
    if (numero%2 == 0):
        return "Es par"
    else:
        return "Es impar"
 

#EJERCICIO 3 

def max(num1, num2, num3):
    """
    Que hace: encuentra el maximo entre tres numeros
    paremetros: numeros
    Devuelve: el numero maximo
    """
    lista_numeros = [num1, num2, num3]
    maximo = None
    for max in lista_numeros:
        if (maximo == None or max > maximo):
            maximo = max
    return maximo

#EJERCICIO 4

def potencia(base, exponente):
    """
    Calcula la potencia de un número.

    Parámetros:
        base (float): La base de la potencia.
        exponente (float): El exponente de la potencia.

    Devuelve:
        float: El resultado de elevar la base al exponente.
    """
     
    resultado = base ** exponente
    return resultado





while(True):
    print("""
        1.- Radio de un circulo /n,
        2.- Numero par o impar /n,
        3.- Numero maximo /n,
        4.- Potencia de un numero /n,

        """
          )
    respuesta = int(input("ingrese una opcion del 1 al 4: "))
    while respuesta <= 0 or respuesta > 4:
        respuesta = int(input("INCORRECTO. ingrese una opcion del 1 al 4: "))

    match(respuesta):
        case 1:
            radio = int(input("ingrese el radio de un circulo: "))
            print(f"El area del circulo es: {calcular_area_circulo(radio)}")
        case 2:
            numero =  int(input("ingrese un numero: "))
            print(f"El numero es:{par_impar(numero)} ")
        case 3:
            num1 =  int(input("ingrese un numero: "))
            num2 =  int(input("ingrese un numero: "))
            num3 =  int(input("ingrese un numero: "))

            print(f"El numero maximo es: {max(num1, num2, num3)}")
        case 4:
            base = int(input("ingrese la base: "))
            exponente = int(input("ingrese el exponente: "))
            print(f"El resultado es: {potencia(base, exponente)}")
        case __:
            break

