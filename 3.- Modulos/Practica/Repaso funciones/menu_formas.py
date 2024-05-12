
#Alumno: Camila Daraio. 
#Falta entregar


from funciones import *

while(True):
    print("""MENU CALCULADORA\n
        1.Ingresar Primer Operando\n
        2.Ingresar Segundo Operando\n
        3.Calcular datos del triangulo rectangulo (Hipotenusa y angulos, area, perimetro)\n
        4.Calcular datos rectangulo (Diagonal, area, perimetro, relacion de aspecto)\n
        5.Calcular datos cuadrado (Diagonal, area, perimetro)\n
        6.Imprimir datos guardados\n
        7.Borrar datos guardados\n
        8.Salir""")
    opcion = int(input("Ingrese una opcion: "))

    match opcion:
        case 1:
            A = pedir_entero("Ingrese el primer valor: ", "Ingrese un valor valido: ", -1000, 1000)
            print("Numero tomado")
        case 2:
            B = pedir_entero("Ingrese el segundo valor: ", "Ingrese un valor valido: ", -1000, 1000)
            print("Numero tomado")
        case 3:
            print("Calcular datos del triangulo rectangulo (Hipotenusa y angulos, area, perimetro)")
            hipotenusa = calcular_hipotenusa(A,B)
            angulos = calcular_angulos(A,B)
            area = calcular_area_triangulo_rectangulo(A,B)
            perimetro = calcular_perimetro_triangulo_rectangulo(A,B)
        case 4:
            print("Calcular datos rectangulo (Diagonal, area, perimetro, relacion de aspecto)")
            angulos = calcular_angulos(A,B)
            area = calcular_area(A,B)
            perimetro = calcular_perimetro(A,B)
        case 5:
            print("Calcular datos cuadrado (Diagonal, area, perimetro)")
        case 6:
            print("Imprimir datos guardados")
        case 7:
            print("Borrar datos guardados")
        case 8:
            print("Salir")