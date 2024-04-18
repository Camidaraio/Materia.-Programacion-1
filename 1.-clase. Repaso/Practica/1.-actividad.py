# La división de higiene está trabajando en un control de stock para productos sanitarios.
# Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
# 1. El tipo (validar "barbijo", "jabón" o "alcohol")
# 2. El precio: (validar entre 100 y 300)
# 3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
# 1000 unidades)
# 4. La marca y el Fabricante.
# Se debe informar lo siguiente:
# A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
# B. Del ítem con más unidades, el fabricante.
# C. Cuántas unidades de jabones hay en total.

barijo_mas_caro = None
cantidad_unidades = None
fabricante_mas_caro = None

mas_unidades = 0
fabricante_mas_unidades = None

contador_jabones = 0


for i in range(5):
    tipo_ingresado = input("ingrese 5 productos: ")

    while (tipo_ingresado != "barbijo" and tipo_ingresado != "jabon" and tipo_ingresado != "alcohol"):
        tipo_ingresado = input("ingrese un tipo valido: ")
    
    precio_ingresado = float(input("ingrese el precio de cada producto: "))

    while (precio_ingresado < 100 or precio_ingresado > 300):
        precio_ingresado = float(input("ingrese un precio valido: "))
    
    cantidad_unidades = int(input("ingrese la cantidad de unidades: "))


    while cantidad_unidades <= 0 or cantidad_unidades > 1000:
        cantidad_unidades = int(input("ingrese una cantidad valida: "))

    fabricante = input("Ingrese el fabricante/marca: ")

    print("pase la validacion")


    # A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.

    if tipo_ingresado == "barbijo" and (barijo_mas_caro == None or precio_ingresado > barijo_mas_caro):
            barijo_mas_caro = precio_ingresado
            fabricante_mas_caro = fabricante


    # B. Del ítem con más unidades, el fabricante.


    if  cantidad_unidades > mas_unidades:
        mas_unidades = cantidad_unidades
        fabricante_mas_unidades = fabricante

    # C. Cuántas unidades de jabones hay en total.

    if tipo_ingresado == "jabon":
        contador_jabones += cantidad_unidades


print("DATOS: \n",
    "A) El precio mas caro pagado por el barbijo es: ", barijo_mas_caro, "y es fabricado por: ", fabricante_mas_caro, "\n",
    "B) El item con mas unidades es: ", fabricante_mas_unidades, "y es: ", mas_unidades, "\n",
    "C) la cantidad de jabones es: ", contador_jabones, "\n" 
    )