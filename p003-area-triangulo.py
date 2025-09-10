# p003-area-triangulo.py
# Calcula el área de un triangulo 

print("Calculando el área de un triángulo")

#Entrada 
print("Dame la base y la altura separados por un ENTER")

base, altura= int(input()), int(input()) # Lee varios valores en una sola entrada 
area= base*altura/2

#Salida
print("El triángulo de base   :", base )
print("El Triángulo de altura :", altura)
print("Tiene un área de       :", area)

print(f"\nEl triángulo de base {base}, y altura {altura}, tiene un área de: {area:.2f}")

print( "El triángulo de base " + str(base) + ", y altura " + str(altura) + ", tiene un área de: " + str(area))