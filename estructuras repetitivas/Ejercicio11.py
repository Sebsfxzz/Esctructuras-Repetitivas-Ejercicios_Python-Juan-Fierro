# definicion de contadores y sumadores
contadorHombres = 0
contadorMujeres = 0
sumaAltura = 0
contadorMayorA170 = 0
contadorMenorOIgualA150 = 0
# ciclo para ingrsar datos de los alumnos
while True:
    edadAlumno = int(input("Ingrese la edad del alumno (Ingrese 0 para finalizar): "))
    if edadAlumno == 0:
        break
    
    sexoAlumno = input("Ingrese el sexo del alumno (H/M): ").upper()
    alturaAlumno = float(input("Ingrese la altura del alumno (en cm): "))
    
    sumaAltura += alturaAlumno
#actualizacion de contadores segun el sexo    
    if sexoAlumno == 'H':
        contadorHombres += 1
    elif sexoAlumno == 'M':
        contadorMujeres += 1
# contadores de altura    
    if alturaAlumno > 170:
        contadorMayorA170 += 1
    elif alturaAlumno <= 150:
        contadorMenorOIgualA150 += 1
# calculo del promedio de la altura
totalAlumnos = contadorHombres + contadorMujeres

if totalAlumnos > 0:
    promedioAltura = sumaAltura / totalAlumnos
else:
    promedioAltura = 0

# Imprimir los resultados
print(f"Cantidad de hombres: {contadorHombres}")
print(f"Cantidad de mujeres: {contadorMujeres}")
print(f"Altura promedio: {promedioAltura:.2f} cm")
print(f"Cantidad de alumnos con altura mayor a 1.70 cm: {contadorMayorA170}")
print(f"Cantidad de alumnos con altura menor o igual a 1.50 cm: {contadorMenorOIgualA150}")
