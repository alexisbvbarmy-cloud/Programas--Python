## p070-conteo-descendente-for-v2.py
## Imprime los números de n a 1, en decrementos de m 

print('\033[2J\033[H')
print("Iniciando secuencia ascendente: ")

n= int(input("Desde dónde?: "))
m= int(input("De cuánto en cuánto?: "))

for f in range(n,0,-m):
    print(f, end=" ")