# p019-calculo-tiempo.py
# Determina el equivalente en días, minutos y segundos de una cantidad de horas dada

print("-"*40)
print("Calculadora de Tiempo")
print("-"*40)

# Entrada
print("Ingresa un número de horas")
horas= int(input())

# Proceso
dias= horas/24
minutos= horas*60
segundos= horas*(60**2)

# Salida
salida=(f"Resultados de conversión\n"
f"El equivalente de {horas} horas en Días es: {dias} días\n"
f"El equivalente de {horas} horas en Minutos es: {minutos} minutos\n"
f"El equivalente de {horas} horas en Segundos es: {segundos} segundos")
print(f"{salida}")
print("-"*40)