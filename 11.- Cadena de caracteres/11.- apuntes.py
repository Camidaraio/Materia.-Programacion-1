"""
Cadena de caracteres: str

"""

# ---- Distintos tipos de metodos ----

"""
strip: Elimina todos los caractes vacios del principio y del final que pueda contener la variable 
"""

#-- EJEMPLO --

variable = "     hola mundo   "
    #print(len(variable))
variable_sin_espacios = variable.strip()
    #print(len(variable_sin_espacios))


"""
variable.lower(): El método lower convertirá a las letras en minúsculas.
"""

#-- EJEMPLO --


cadena = "Hola Mundo"
cadena = cadena.lower()
    #print(cadena) # hola mundo

"""
variable.upper(): convertirá a las letras en mayúsculas.
"""

#-- EJEMPLO --

cadena = "Hola Mundo"
cadena = cadena.upper()
    #print(cadena) # HOLA MUNDO

"""
variable.capitalize():convertirá a la primera letra de la Strings en mayúscula y el resto en
minúscula.
"""

#-- EJEMPLO --

cadena = "hola Mundo"
cadena = cadena.capitalize()
    #print(cadena) # Hola mundo 


"""
replace remplazará un conjunto de caracteres por otro.
"""

#-- EJEMPLO --

cadena = "Hola Mundo"
cadena = cadena.replace("la","@")
    #print(cadena) # Ho@ Mundo


"""
split(): divide una cadena en subcadenas y las devuelve almacenadas en una lista.
"""

#-- EJEMPLO --

cadena = "Python,Java,C"
    #print(cadena.split(","))
    #['Python', 'Java', 'C']

"""
variable.join(): devuelve la primera cadena unida a cada uno de los elementos de la lista que se le pasa como parámetro.
"""

#-- EJEMPLO --

separador = "+"
cadena = separador.join(["A", "B", "C"])
    #print(cadena) # A+B+C


"""
zfill(): rellena la cadena con ceros a la izquierda hasta llegar a la longitud pasada como parámetro.
"""

#-- EJEMPLO --

cadena = "314"
    #print(cadena.zfill(6))
    #000314


"""
isalpha(): devuelve True si todos los caracteres son alfabéticos, False de lo contrario.
"""

#-- EJEMPLO --

cadena = "Hola Mundo"
    #print(cadena.isalpha())
    # False -> por el espacio
cadena = "HolaMundo"
    #print(cadena.isalpha())
    # True

"""
isalnum(): devuelve True si todos los caracteres son alfanuméricos, False de lo contrario.
"""

#-- EJEMPLO --

cadena = "Hola Mundo 123"
    #print(cadena.isalnum())
    # False -> por el espacio
cadena = "HolaMundo123"
    #print(cadena.isalnum())
    # True


"""
isnumeric(): devuelve True si todos los caracteres son numéricos (incluido números romanos, fracciones, etc), False
de lo contrario. Tampoco puede haber espacios
"""

#-- EJEMPLO --

cadena = "josesito2020"
    #print(cadena.isnumeric())
    # False -> por el ‘josesito’
cadena = "2020"
    #print(cadena.isnumeric())
    # True



"""
count(): permite contar las veces que otra cadena se encuentra dentro de la primera.
"""

#-- EJEMPLO --

cadena = "Hola Mundo Hola"
#   print(cadena.count("la")) # 2

"""
format las llaves, llamadas campos de formato, son reemplazadas con los valores de
las variables pasadas.
"""

#-- EJEMPLO --

nombre_usuario="JUAN"
edad_usuario=35
cadena = "Nombre: {1}, Edad: {0}"
    #print(cadena.format(edad_usuario,nombre_usuario))
    #Nombre: JUAN, Edad: 35


"""
f-strings(): permiten incrustar expresiones dentro de cadenas.
"""

#-- EJEMPLO --

n_usuario="JUAN"
e_usuario=35
cadena = f"Nombre: {n_usuario}, Edad: {e_usuario}"
    #print(cadena)
    #Nombre: JUAN, Edad: 35

"""
len(): indica la longitud de la cadena de texto dentro de la variable en ese momento.
"""

#-- EJEMPLO --

cadena = "Hola Mundo"
    #print(len(cadena)) # 10

"""
slice(): (rebanada), el primer número es donde comienza (inclusivo), y el segundo
número de índice es donde termina (exclusivo).
"""

#-- EJEMPLO --

cadena = "Hola Mundo"
print(cadena[5:10]) # Mundo
print(cadena[5:]) # Mundo
print(cadena[:5]) # Hola