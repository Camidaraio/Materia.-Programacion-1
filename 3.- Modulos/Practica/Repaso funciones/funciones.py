#Alumno: Camila Daraio. 
#Falta entregar

def pedir_entero(mensaje, mensaje_error, minimo, maximo):
    """
    Validacion de la opcion ingresada
    """
    entero_ingresado = int(input(mensaje))
    while entero_ingresado < minimo or entero_ingresado > maximo:
        entero_ingresado = int(input(mensaje_error))
    return entero_ingresado

# triangulo rectangulo

def calcular_hipotenusa(cateto1, cateto2):
    """
    Calcula la hipotenusa
    """
    hipotenusa = (cateto1**2 + cateto2**2)**0.5
    return hipotenusa

def calcular_angulos(cateto1, cateto2):
    """
    Calcula los ángulos de un triángulo rectángulo.
    """
    angulo_agudo = cateto1 / cateto2
    angulo_recto = 90.0

    return angulo_agudo, angulo_recto


def calcular_area_triangulo_rectangulo(cateto1, cateto2):
    """
    Calcula el area de un triangulo rectangulo
    """
    area = (cateto1 * cateto2) / 2
    return area

def calcular_perimetro_triangulo_rectangulo(cateto1, cateto2):
    """
    calcula el perimetro de un triangulo rectangulo
    """
    hipotenusa = calcular_hipotenusa(cateto1, cateto2)
    perimetro = cateto1 + cateto2 + hipotenusa
    return perimetro


# rectangulo

def calcular_area(lado1, lado2):
    """
    Calcula el área de un rectángulo.

    Parámetros:
        lado1 (float): Longitud del primer lado.
        lado2 (float): Longitud del segundo lado.

    Retorna:
        Área del rectángulo.
    """
    area = lado1 * lado2
    return area


def calcular_perimetro(lado1, lado2):
    """
    Calcula el perímetro de un rectángulo.

    Parámetros:
        lado1 (float): Longitud del primer lado.
        lado2 (float): Longitud del segundo lado.

    Retorna:
        float: Perímetro del rectángulo.
    """
    if lado1 is None or lado2 is None:
        print("Error: Debe ingresar la longitud de los lados del rectángulo.")
        return None

    perimetro = 2 * (lado1 + lado2)
    return perimetro