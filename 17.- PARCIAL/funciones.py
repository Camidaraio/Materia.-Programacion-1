import csv

def pedir_entero(mensaje : str, error: str, desde: int, hasta: int):
    """"""
    while True:
        entrada = input(mensaje)
        if entrada.isnumeric():
            entero = int(entrada)
            if desde <= entero <= hasta:
                #print("ingresado correctamente")
                return entero
            else:
                print(error)
        else:
            print(error)


