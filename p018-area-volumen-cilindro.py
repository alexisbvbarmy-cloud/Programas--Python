# p018-area-volumen-cilindro.py
# Calcula el área y el volumen de un cilindro 

print("-"*40)
print("Calculadora para área y volumen de un cilindro")
print("-"*40)

# Entrada 
print("Ingresa el radio y la altura del cilindro en centímetros, separados por un ENTER")
r, h= float(input()), float(input())

# Proceso 
import math as mt
a= (2*(mt.pi*mt.pow(r,2)))+ (2*(mt.pi*r*h))
v= mt.pi*(mt.pow(r,2))*h

# Salida 
salida=(f"Resumen de operaciones\n"
f"El radio del cilindro mide: {r:.2f}\n"
f"La altura del cilindro es: {h:.2f}\n"
f"=> El área del cilindro es: {a:,.4f} centímetros cúbicos\n"
f"=> El volumen del cilindro es: {v:,.4f} centrímetros cúbicos")
print(f"{salida}")
print("-"*40)