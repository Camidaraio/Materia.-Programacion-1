from funciones import *

## CAMILA DARAIO

def menu():
    while(True):
        A = None
        B = None

        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        
        opcion = pedir_entero("Ingrese un numero: ", "Ingrese un numero entre 1 y 5: ", 1, 5)

        
        
        if opcion == 1:
            A = pedir_entero("Ingrese un valor: ", "Ingrese un valor valido: ", -1000, 1000)
            print("Numero tomado")
        elif opcion == 2:
            B = pedir_entero("Ingrese un valor: ", "Ingrese un valor valido: ", -1000, 1000)
            print("Numero tomado")

        elif opcion == 3:
            if A is None or B is None:
                print("debe ingresar los numeros")
            else:
                suma = calcular_suma(A,B)
                resta = calcular_resta(A,B)
                division = calcular_división(A,B)
                multiplicación = calcular_multiplicacion(A,B)
                potencia = calcular_potencia(A,B)
                factorial_A = calcular_factorial(A)
                factorial_B = calcular_factorial(B)

        elif opcion == 4:
            if A is None or B is None:
                print("debe ingresar los numeros")
            else:
                print(f"El total de la suma es: {suma}")
                print(f"El total de la resta es: {resta}")
                print(f"El total de la division es: {division}")
                print(f"El total de la multiplicación es: {multiplicación}")
                print(f"El total de la potencia es: {potencia}")
                print(f"El total de la factorial de A es: {factorial_A}")
                print(f"El total de la factorial de B es: {factorial_B}")

                

        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")


menu()
