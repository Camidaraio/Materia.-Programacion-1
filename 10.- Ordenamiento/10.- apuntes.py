#Alumna: Camila Daraio
# Debo repasar la clase


numeros = [5,3,1,7,9]

#ORDENO DE MAYOR A MENOR
for i in range(len(numeros)):
    for j in range(i+1,len(numeros),1):
        if(numeros[i] < numeros[j]):
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux

print(numeros)