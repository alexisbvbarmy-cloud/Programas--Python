# p006-conversor-temp.py
# Convertir temperatura de Celsius a Fahrenheit

print("Comversor de Temperatura (Celsius a Fahrenheit)\n")

#Entrada
celsius= float(input("Ingresa la temperatura en Celsius: "))

#Proceso 
fahrenheit= (celsius*9/5)+32

#Salida
print(f"La temperatura en Fahrenheit es {fahrenheit:.2f}°F")