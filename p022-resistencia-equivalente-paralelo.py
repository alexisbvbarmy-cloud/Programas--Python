# p022-resistencia-equivalente-paralelo.py
# Calcular la Resistencia Total o Equivalente con 4 resistencias en paralelo

print("-"*40)
print("Calculo de Resistencia Total")
print("-"*40)

# Entrada
print("Ingresa el valor de las 4 resistancias en paralelo, separadas por un espacio")
r1,r2,r3,r4= input().split()
r1,r2,r3,r4= int(r1), int(r2), int(r3), int(r4)

# Proceso
rt= 1/(1/r1+1/r2+1/r3+1/r4)

# Salida 
print(f"La Resistencia Total es: {rt:,.4f}")
print("-"*40)