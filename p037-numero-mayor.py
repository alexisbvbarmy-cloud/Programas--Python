## p037-numero-mayor.py
## Pide tres números enteros e identifica y muestra cuál de ellos es mayor 

print("\033[2j\033[H")
print("-----Determinar El número Mayor-----")
print("Ingresa tres números enteros separados por un espacio:")
n1, n2, n3, = input().split()
n1, n2, n3, = int(n1), int(n2), int(n3)

# Proceso
if n1>n2 and n1>n3:
    print(f"El número mayor es: {n1}")
elif n2>n1 and n2>n3:
    print(f"El número mayor es: {n2}")
elif n3>n1 and n3>n2:
    print(f"El número mayor es: {n3}")

print("\nProceso Terminado")