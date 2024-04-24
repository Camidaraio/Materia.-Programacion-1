def sumar_naturales(numero:int):
    if numero == 1:
        return 1
    else:
        resultado = numero + sumar_naturales(numero - 1)
        return resultado
    

def calcular_potencia(base:int, exponente:int):
    if base == 1:
        return 1
    else:
        resultado = base ** calcular_potencia(base - 1)
        return resultado





# print(sumar_naturales(10))


def sumar_digitos(numero: int) -> int:
    if numero < 10:
        return 0
    else:
        resultado = numero % 10 + sumar_digitos(numero // 10)

    return resultado

print(sumar_digitos(3))


 
