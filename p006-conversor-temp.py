# p006-conversor-temp.py
# Convertir temperatura de Celsius a Fahrenheit

print("Comversor de Temperatura (Celsius a Fahrenheit)\n")

#Entrada
celsius= float(input("Ingresa la temperatura en Celsius: "))

#Proceso 
fahrenheit= (celsius*9/5)+32

#Salida
print(f"La temperatura en Celsius de {celsius:.2f} equivale a {fahrenheit:.2f}°F")