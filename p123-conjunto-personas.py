## p123-conjunto-personas.py
## Crear y mostrar los conjuntos A (lista 1) y B (lista 2)
## Calcular y mostrar los resultados de:
# Unión (A|B)
# Intersección (A&B)
# Diferencia (A-B)
# Diferencia Simétrica (A^B)
## Verificar y mostrar
# ¿Es {Pablo, Mateo} un subconjunto de B?
# ¿Es A un superconjunto de {Reynaldo, Angelica}?
# ¿Está "Pedro" en el conjunto A?
# ¿No está "Lilia" en el conjunto B?

lista1= ["Juan", "Maria", "Pedro", "Jose", "Rocio" ]
lista2= ["Pedro", "Juan", "Pablo", "Mateo", "Esther"] 

print('\033[H\033[J')
print("Conjuntos")

c_A= set(lista1)
c_B= set(lista2)
print(f"Conjunto A: {c_A}\nConjunto B: {c_B}")

print("\nUnión: ")
print(f"Conjunto A unión Conjunto B: {c_A.union(c_B) }")

print("\nIntersección")
print(f"Conjunto A intersección Conjunto B: {c_A.intersection(c_B) }")

print("\nDiferencia")
print(f"Conjunto A diferrencia Conjunto B: elementos de c_A que no están en c_B {c_A.difference(c_B) }")

print("\nDiferencia simétrica")
print(f"Conjunto A diferencia simétrica Conjunto B: elementos en uno u otro conjunto {c_A.symmetric_difference(c_B) }")

print("\nSubconjuntos")
sub_c= {"Pablo", "Mateo"} <= c_B
print(f"Es {"Pablo", "Mateo"} subconjunto de Conjunto B? {sub_c}")

print("\nSuperconjuntos")
sup_c= c_A >= {"Reynaldo", "Angelica"}
print(f"Es A un superconjunto de {"Reynaldo", "Angelica"}? {sup_c}")

print("\nPertenencia o no pertenencia a un conjunto")
not_pedro= "Pedro" in c_A
print(f"Está 'Pedro' en c_A? {not_pedro}")
not_lilia= "Lilia" not in c_B
print(f"Está Lilia en c_B? {not_lilia}")