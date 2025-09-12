# p021-distancia-entre-puntos.py
# Calcular la distancia entre dos puntos en un plano cartesiano

print("-"*40)
print("Distancia entre dos puntos")
print("-"*40)
import math as mt

# Entrada
print("Ingresa las coordenadas X y Y del punto A separadas por ENTER")
x1, y1= int(input()), int(input())
print("Ingresa las coordenadas X y Y del punto B separadas por ENTER")
x2, y2= int(input()), int(input())

# Proceso
d= mt.sqrt(mt.pow(x1+x2,2)+mt.pow(y1+y2,2))

# Salida 
print(f"La distancia entre los puntos A y B es: {d:,.4f}")
print("-"*40)