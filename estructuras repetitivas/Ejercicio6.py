# definir las variables de hombres y mujeres
cantidadPersonas = int(input("Ingrese la cantidad total de personas en el salón: "))
contadorHombres = 0
contadorMujeres = 0
#varible de bucle es para defenir el sexo de la persona
for i in range(cantidadPersonas):
    sexoPersona = input("Ingrese el sexo de la persona (H/M): ").upper()
    if sexoPersona == 'H':
        contadorHombres += 1
    elif sexoPersona == 'M':
        contadorMujeres += 1
# imprimir el resultado
print(f"Hombres: {contadorHombres}, Mujeres: {contadorMujeres}")