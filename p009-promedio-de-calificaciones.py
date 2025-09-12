# p009-promedio-de-calificaciones.py 
# Calcular el promedio de 3 calificaciones ingresadas por el usuario

print("Calculando el promedio de tres calificaciones")

# Solicitar 3 calificaciones separadas por un espacio
cal1, cal2, cal3= input().split()
print(type(cal1), type(cal2), type(cal3))

cal1, cal2, cal3= int(cal1), int(cal2), int(cal3) # convertir cada variable de cadena a entrero     
print(type(cal1), type(cal2), type(cal3))

# Calcular el promedio
prom= (cal1 + cal2 + cal3) /3

# Moostrar el resultado
print(f"Las calificaciones son: {cal1}, {cal2}, {cal3}")
print(f"El promedio es: {prom}")

    