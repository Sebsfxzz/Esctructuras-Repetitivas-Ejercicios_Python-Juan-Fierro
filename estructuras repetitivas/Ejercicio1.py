#definir las variables de los numeros
num_Positivos=0
num_Negativo=0
num_Neutro=0
#leer los 20 numeros
for i in range (20):
    numero=int(input("ingrese numero: "))

    if numero > 0:
        num_Positivos+=1
    elif numero <0:
        num_Negativo+=1
    else:
        num_Neutro+=1
#impresion de la clasificacion de los numeros
print(f"estos son los numeros positivos: {num_Positivos} , los numeros negativos son: {num_Negativo} , los numeros neutros son: {num_Neutro}")



