## p039-conteo-descendente-v2.py
## Imprime los números de n a 1, usando un ciclo while

print("\033[2j\033[H")
print("Iniciando Cuenta Regresiva")

n= int(input("Desde dónde incia el conteo: "))
n= int(input("De cuanto en cuanto: "))

c=n

while c>=1:
    print(f"{c}", end="")
    c-=1

print("\nTerminado...")