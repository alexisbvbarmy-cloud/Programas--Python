## p124-conjunt-numeros.py
## Crear y mostrar los conjuntos A(lista1), B(lista2) y C(lista3)
## Calcular y mostrar los resultados de:
# Unión (A|B)
# Unión (B | C)
# Diferencia (A - C)
# Diferencia Simétrica (B ^ C)
# Intersección (B & C)
## Verificar y mostrar
# ¿Es A subconjunto de B?
# ¿Es C subconjunto de A?
# ¿Está el número 100 en A?
# ¿Está el número 60 en A, B y C?
# ¿No está el número 900 en C?

lista_1= [50, 60, 70, 80, 90, 100, 200]
lista_2= [60, 90, 100, 300, 400, 500]
lista_3= [10, 20, 60, 90, 70, 100, 600, 700]

print('\033[H\033[J')
print("Conjuntos de Números")

cA= set(lista_1)
cB= set(lista_2)
cC= set(lista_3)
print(f"Conjunto A: {cA}\nConjunto B: {cB}\nConjunto C: {cC}")

print("\nUnión: ")
print(f"Conjunto A unión Conjunto B: {cA.union(cB) }")
print(f"Conjunto B unión Conjunto C: {cB | cC }")

print("\nDiferencia")
print(f"Conjunto A diferencia Conjunto C: {cA.difference(cC)}")

print("\nDiferencia simétrica")
print(f"Diferencia simétrica (B ^ C): elementos en uno u otro conjunto {cB.symmetric_difference(cC)}")

print("\nIntersección")
print(f"Intersección (B & C): {cB.intersection(cC) }")

print("\nPertenencia o no pertenencia a un conjunto")
print(f"¿Es A subconjunto de B? {cA.issubset(cB)}")
print(f"¿Es C subconjunto de A? {cC.issubset(cA)}")
print(f"¿Está el número 100 en A? {100 in cA}")
print(f"¿Está el número 60 en A, B y C? {100 in cA, cB, cC}")
print(f"¿No está el número 900 en C? {900 not in cC}")