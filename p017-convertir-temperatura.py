# p017-convertir-temperatura.py
# Convertir temperatura de grados Celsius a Fahrenheit  

print("-"*40)
print("Conversor de temperatura de grados Celsius a grados Fahrenheit")
print("-"*40)

# Entrada
print("Ingresa la temperatura en grados Celsius")
t= int(input())

# Conversion
f= (t*9/5)+32

# Salida 
print(f"La temperatura en grados Fahrenheit es: {f:.2f}°")
print("-"*40)