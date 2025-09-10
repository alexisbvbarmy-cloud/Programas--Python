# p002-area-circulo.py
# Calcula el área de un círculo: área= (pi*r*r)

import math # Importar el módulo math para constantes y funciones matemáticas

print("Calculando el área de un círculo: \n")

# Entrada   
print("Dame el radio: ")
radio= float (input())

# Proceso   
area= math.pi*math.pow(radio,2)

# Salida
print(f"El círculo de radio {radio:.2f} tiene un área de: {area:,.2f}")