#definir las variables de los numeros 
sumaPositivo=0
#leer 10 numeros negativos
for i in range(10):
    numero = float(input(f"ingrese un numero negativo{i + 1}: "))
    if numero<0:
        numeroPositivo = abs(numero)
        sumaPositivo+=numeroPositivo
    else:
        print("el nuemro ingresado es negativo")
print(f"la suma de los numeros convertidos postivos es {sumaPositivo}")