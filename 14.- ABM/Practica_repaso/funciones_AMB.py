# Funciones de AMB

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

def pedir_str(mensaje : str, error: str):
    """"""
    while True:
        entrada = input(mensaje)
        if entrada.isalpha():
            #print("ingresado correctamente")
            return entrada.capitalize()
        else:
            print(error)
            

def listar_alumnos(lista_alumnos):
    for alumno in lista_alumnos:
        mensaje = ''
        for clave, valor in alumno.items():
            mensaje += f"|| {clave} || {valor} "
        print(mensaje)


def modificar_alumnos(legajo: int, lista_alumnos: list, clave: str, valor : any):
    """"""
    alumno_encontrado = False
    for i in range(len(lista_alumnos)):
        if lista_alumnos[i]["Legajo"] == legajo:
            lista_alumnos[i][clave] = valor
            alumno_encontrado = True
            break
    return alumno_encontrado

def mostrar_claves(diccionario: dict):
    claves = diccionario.keys()
    for clave in claves:
        print(clave)



    
def agregar_alumno(nombre, apellido, legajo, Nota_final, estado, lista_alumnos):
    """"""
    nuevo_alumno = {"Nombre": nombre, "Apellido": apellido, "Legajo": legajo, "Nota_final": Nota_final, "Estado": estado}
    lista_alumnos.append(nuevo_alumno)
