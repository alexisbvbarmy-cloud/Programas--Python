# p015-hipotenusa-triangulo
# Crear un programa que calcule la longitud de la hipotenusa de un triángulo rectángulo 

print("-"*40)
print("Calculo de la hipotenusa de un triángulo rectángulo")
print("-"*40)
# Entrada 
print("Ingresa la longitud de los dos catetos separados por un espacio")
c1, c2= input().split()
c1,c2= float(c1), float(c2)

# Proceso 
import math as mt
hip= mt.sqrt(c1**2 + c2**2)

# Salida 
salida=(f"Resumen de operaciones\n"
f"La longitud del coseno 1 es: {c1:.2f}\n"
f"La longitud del coseno 2 es: {c2:.2f}\n"
f"La longitud de la hipotenusa es: {hip:.4f}")
print(f"{salida}")
print("-"*40)