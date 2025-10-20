## p102-listas-aleatorios-suma.py
## Generar 2 listas de 10 números aleatorios cada una. 
## Crear una tercera lista donde el elemento sea la suma de los correpodientes de ls listas A y B, sólo si ambos elementos son impares, de lo contrario, el elemento de la tercera lista será 0. imprimir las 3 listas. }

import random

print('\033[2J\033[H')
print("Sumar números en dos listas de números aleatorios")

lista1= [random.randint(1,100) for _ in range (10)]
lista2= [random.randint(1,100) for _ in range (10)]

lista3 = [lista1[i] + lista2[i] if (lista1[i] % 2 != 0 and lista2[i] % 2 != 0) else 0 for i in range(10)]

print("\n" + "="*50)
print("RESULTADOS:")
print("="*50)
print(f"Lista A: {lista1}")
print(f"Lista B: {lista2}")
print(f"Lista C: {lista3}")