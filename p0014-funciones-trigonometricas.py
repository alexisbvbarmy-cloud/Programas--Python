# p0014-funciones-trigonometricas.py
# Demostrar el uso de funciones trigonométricas básicas

print("-"*40)
print("Operadores de Asignación en Python")
print("-"*40)
import math as mt

# Definir un ángulo en grados y convertirlo en radianes 
angulo= 45
radianes= mt.radians(angulo)

# Calcular funciones triginométricas básicas 
seno= mt.sin(radianes)
coseno= mt.cos(radianes)
tangente= mt.tan(radianes)

# cpnvertir de cuelta a grados para demostración 
grados= mt.degrees(radianes)

# Formatear la salida con f-strings para mejor presentación 
salida= ("Resumen de funciones\n"
f"El seno es {seno:.4f}\n" 
f"El coseno es {coseno:.4f}\n"  
f"La tangente es {tangente:.4f}\n"  
f"El ángulo de {angulo} grados, en radianes equivale a {radianes:.4f}\n"  
f"Los radianes {radianes:.4f} equivañen a {grados:.1f}°\n")

# Mostrar la salida formateada
print(salida)
print("-"*40)