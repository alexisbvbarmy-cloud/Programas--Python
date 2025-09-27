## p036-numeros-consecutivos.py
## Determinar si tres números son consecutivos

print("\033[2j\033[H")
print("-----Determinar si tres números son consecutivos-----")
print("Ingresa tres números enteros separados por un espacio:")
n1, n2, n3, = input().split()
n1, n2, n3, = int(n1), int(n2), int(n3)

# Proceso
if n2==(n1+1) and n3==(n2+1):
    print("\nLa secuencia de números es consecutiva")
elif n1<n2<n3:
    print("\nLos números no son consecutivos pero siguen una secuencia ascendente")
else:
    print("\nLos números NO son consecutivos")

print("\nProceso Terminado")
