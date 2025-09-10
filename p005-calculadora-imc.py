# p005-calculadora-imc.py
# Calcular el IMC de una persona

# Entrada
print("Calculadora de ïndice de Masa Corporal")
peso_kg= float(input("Ingresa tu peso en kilogramos \n"))
altura_m= float(input("Ingresa tu altura en metros \n"))

# Proceso 
imc= peso_kg/(altura_m**2) #divide el peso entre la altura al cuadrado (** eleva a la potencia66)

#Salida
print("\nEl peso es {0:.2f}kg, la altura es {1:.2f}m, esto resulta en un IMC de {2:.2f}".format(peso_kg,altura_m,imc))

print(f"\nEl peso es {peso_kg:.2f}kg, la altura es {altura_m:.2f}, por lo tanto tu Índice de Masa Corporal es: {imc:.2f}")