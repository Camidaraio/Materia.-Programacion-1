## CAMILA DARAIO

def primer_numero ():
    ''''''
    numero_1 = int(input("ingrese el primer numero a operar: "))
    return numero_1

def segundo_numero ():
    ''''''
    numero_2 = int(input("ingrese el segundo numero a operar: "))
    return numero_2

def pedir_entero(mensaje, mensaje_error, minimo, maximo):
    """
    Validacion de la opcion ingresada
    """
    entero_ingresado = int(input(mensaje))
    while entero_ingresado < minimo or entero_ingresado > maximo:
        entero_ingresado = int(input(mensaje_error))
    return entero_ingresado



def calcular_suma(A,B):
    ''''''
    suma = A + B
    return suma


def calcular_resta(A,B):
    '''
    '''
    resta = A - B
    return resta

def  calcular_división (A,B):
    ''' Division'''
    if B != 0:
        división  = A / B
        return  división 
    else: 
        print("No es posible dividir por 0, intenta con otro numero")

def  calcular_multiplicacion (A,B):
    ''''''
    multiplicacion  = A  * B
    return  multiplicacion 

def  calcular_potencia (A,B):
    ''''''
    potencia  = A ** B
    return  potencia 



def  calcular_resto (A,B):
    ''''''
    if B != 0:
        resto  = A % B
        return  resto 
    else: 
        print("No es posible dividir por 0, intenta con otro numero")



def calcular_factorial(A):
    if A == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, A + 1):
            resultado *= i
        return resultado
