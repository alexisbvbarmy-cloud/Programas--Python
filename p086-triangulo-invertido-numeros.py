## p086-triangulo-invertido-numeros.py
## Solicita un número n que será la altura de un triángulo numérico invertido. 

print('\033[2J\033[H')
print("=== TRIÁNGULO NUMÉRICO INVERTIDO ===\n")

# Solicitar número
n = int(input("Ingrese la altura del triángulo: "))

print(f"\nTriángulo de altura {n}:\n")

# Generar triángulo invertido
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()