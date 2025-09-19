## p025-verificar-suma.py
## Verificar si la suma de dos número ses igual a un tercero 

print("-"*60)
print("Verificar si la suma de dos número ses igual a un tercero")
print("-"*60)

print("\nDame tres npumero enteros")
n1= int(input("Número 1:"))
n2= int(input("Número 2:"))
n3= int(input("Número 3:"))

# Proceso
suma= n1 + n2

if suma == n3:
    print(f"\nCorrecto 👍 {n1} + {n2} es igual a {n3}")
else:
    print(f"\nNo Coninciden ❌ {n1} + {n2} es igual a {n3}")
print("-"*60)
print("\nFin del Programa")