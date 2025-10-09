## p079-factorial-numeros.py
## Calcula el factorial de n números 

print('\033[2H\033[J')
print("Calcula el factorial de 1 a n")

try:
    n=int(input("Cuántos factoriales?: "))
    for i in range(1,n+1):
        factorial=1
        for j in range(1,n+1):
            factorial+=j
        print(f"Factorial de {i}! es = {factorial}")
except ValueError:
    print("Error: Se esperaba un número entero")