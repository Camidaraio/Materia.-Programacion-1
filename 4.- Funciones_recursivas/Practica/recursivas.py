#Alumno: Camila Daraio. 
#Entregado
def sumar_naturales(numero:int):
    if numero == 1:
        return 1
    else:
        resultado = numero + sumar_naturales(numero - 1)
        return resultado
    

def calcular_potencia(base:int, exponente:int):
    if exponente == 0:
        resultado = 1
    else:
        resultado = base * calcular_potencia(base, exponente - 1)
    return resultado


def sumar_digitos(numero: int) -> int:
    if numero < 10:
        resultado = numero
    else:
        ultimo_digito = numero % 10
        digitos_restantes = numero // 10
        resultado = ultimo_digito + sumar_digitos(digitos_restantes)

    return resultado

# # Otra manera
# def sumar_digitos(numero: int) -> int:
#     if numero < 10:
#         return 0
#     else:
#         resultado = numero % 10 + sumar_digitos(numero // 10)

#     return resultado


def calcular_fibonacci(numero):
    if(numero < 2):
        resultado = numero
    else:
        resultado = calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)
    return resultado




 
