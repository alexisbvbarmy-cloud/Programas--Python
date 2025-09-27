## p036-conteo-ascendente.py
## Imprime los números del 1 al 100 usando un ciclo while

print("\033[2j\033[H")
print("Iniciando secuencia ascendente...")

c=1

while c<=200:
    print(f"{c}", end="")
    c+=1

print("\nSecuencia Completada")