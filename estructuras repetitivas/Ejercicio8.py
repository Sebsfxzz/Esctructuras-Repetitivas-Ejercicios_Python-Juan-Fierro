# variables de contadores para las fiferentes categorias de clasificacione 
contadorMenor50 = 0
contadorEntre50y69 = 0
contadorEntre70y79 = 0
contadorMayor80 = 0
# se usa un ciclo for para interar 23 veces, representando a los 23 estudiantes
for i in range(23):
#solicitamos la calificacion del estudiante y la convertimos a un valor flotante
    calificacionEstudiante = float(input("Ingrese la calificación del estudiante (1-100): "))
#verificamos en que rango de calificacion esta el estudiante   
    if calificacionEstudiante < 50:
        contadorMenor50 += 1
    elif 50 <= calificacionEstudiante < 70:
        contadorEntre50y69 += 1
    elif 70 <= calificacionEstudiante < 80:
        contadorEntre70y79 += 1
    else:
        contadorMayor80 += 1
# imprimir los resultados finales
print(f"Menor a 50: {contadorMenor50}, Entre 50 y 69: {contadorEntre50y69}, Entre 70 y 79 {contadorEntre70y79}, Mayor o igual a 80: {contadorMayor80}")