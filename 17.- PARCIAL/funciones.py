from datetime import datetime


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

def solicitar_fecha(prompt):
    """Solicita una fecha y valida que tenga el formato DD/MM/AAAA."""
    while True:
        fecha_str = input(prompt)
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            return fecha
        except ValueError:
            print("Formato de fecha incorrecto. Por favor, use el formato DD/MM/AAAA.")


def solicitar_fechas():
    print("Ingrese las fechas en el formato DD/MM/AAAA.")
    fecha_inicio = solicitar_fecha("Fecha de inicio: ")
    while True:
        fecha_fin = solicitar_fecha("Fecha de fin: ")
        if fecha_fin < fecha_inicio:
            print("La fecha de fin no puede ser anterior a la fecha de inicio. Inténtelo de nuevo.")
        else:
            break
    return fecha_inicio, fecha_fin

#fecha_inicio, fecha_fin = solicitar_fechas()
#como debo mostrar las fechas
# print("Fecha de inicio:", fecha_inicio.strftime("%d/%m/%Y"))
# print("Fecha de fin:", fecha_fin.strftime("%d/%m/%Y"))

def agregar_alumno(nombre, apellido, legajo, Nota_final, estado, lista_alumnos):
    """"""
    nuevo_alumno = {"Nombre": nombre, "Apellido": apellido, "Legajo": legajo, "Nota_final": Nota_final, "Estado": estado}
    lista_alumnos.append(nuevo_alumno)


def pedir_fechas():
    """"""




