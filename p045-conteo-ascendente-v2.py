## p045-conteo-ascendente-v2.py
## Imprime los números de 1 a n en incrementos de m, usando while

print("\033[2j\033[H")
print("Iniciando Secuencia ascendente")

n= int(input("Hasta donde: "))
m= int(input("De cuanto en cuanto:"))
c=1

while c<=n:
    print(f" {c}",end='')
    c+=m
print("\nSecuencia Completada")