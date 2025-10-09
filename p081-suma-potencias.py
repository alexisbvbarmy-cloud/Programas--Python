## p081-suma-potencias.py
## Suma de potencias de un número X, desde X elevado a la 1, hasta X elevado a la n

print('\033[2J\033[H')

x= int(input("Valor de X: "))
n= int(input("Valor de n: "))

suma_total=0
termino_actual=1
for j in range(n+1):
    suma_total+=termino_actual
    print(f"Termino {x} ^ {n} = {termino_actual}")
    termino_actual*=x

print(f"\nSuma de toda la serie: " ,suma_total)