# p016-tercer-angulo.py
# Determina el terce ángulo de un triángulo 

print("-"*50)
print("Determinación del tercer ángulo de un triángulo")
print("-"*50)

# Entrada
print("Ingresa las medidas de dos de los ángulos del triángulo separados por un ENTER")
a1, a2= int(input()), int(input())

# Proceso
a3= 180-(a1+a2)

# Salida
salida=(f"Resumen de operaciones\n"
f"El ángulo 1 mide: {a1:.2f}°\n"
f"El ángulo 2 mide: {a2:.2f}°\n"
f"=> El ángulo 3 mide: {a3:.2f}°")
print(f"{salida}")
print("-"*40)
