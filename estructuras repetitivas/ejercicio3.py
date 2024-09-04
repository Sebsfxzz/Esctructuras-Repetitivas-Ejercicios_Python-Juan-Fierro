#inizializar variables
sumaTotal = 0
calificacionAlta = float("-inf")
calificacionBaja = float("inf")
#leer las calificaciones de 20 alumnos
for i in range(20):
    calificacion=float(input(f"ingrese la calificacion del alumno{i + 1}: "))
# sumar la calificacion a la suma total
    sumaTotal +=  calificacion
#verificar si la calificacion es la mas alta
if calificacion > calificacion:
   calificacionAlta = calificacion
#verifica si la calificacion es la mas baja
if calificacion < calificacionBaja : 
    calificacionBaja = calificacion
# calcula el promedio
promedio = sumaTotal / 20 
#imprimir el promedio, la calificacion mas alta y la mas baja 
print(f"El promedio del grupo es: {promedio}")
print(F"La calificacion mas alta es: {calificacionAlta}")
print(f"la calificacion mas baja es: {calificacionBaja}")