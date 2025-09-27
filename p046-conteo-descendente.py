## p038-conteo-descendente.py
## Imprime los números de 100 a 1, usando un ciclo while

print("\033[2j\033[H")
print("Iniciando Cuenta REgresiva")

c=100

while c>=1:
    print(f"{c}", end="")
    c-=1

print("\nTerminado...")