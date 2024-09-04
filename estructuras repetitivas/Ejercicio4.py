# definir la variable del numero a multiplicar 
numeroMultiplicar = int(input("Ingrese un número para calcular su tabla de multiplicar: "))

for i in range(1, 11):
    productoMultiplicacion = numeroMultiplicar * i
    print(f"{numeroMultiplicar} * {i} = {productoMultiplicacion}")