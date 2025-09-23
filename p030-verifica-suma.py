## p030-verifica-suma.py
## Verificar si la suma de dos números es igual a un tercero
## 

print("\033[2j\033[H")
print("----Verificar si la suma de dos números es igual a un terrcero")

print("Dame tres números separados por un espacio:")
n1, n2, n3, = input().split()
n1, n2, n3, = int(n1), int(n2), int(n3)

# Proceso
if n1+n2==n3:
    print(f"{n1}+{n2} = {n3}!")
elif n1+n3==n2:
    print(f"{n1}+{n3} = {n2}!")
elif n2+n3==n1:
    print(f"{n2}+{n3} = {n1}!")
elif n1==n2==n3:
    print(f"{n1}, {n2}, {n3} son Iguales!")
elif n1 != n2 != n3:
    print(f"{n1}, {n2}, {n3} son Diferentes!")
else:
    print(f"Es probable que {n1}, {n2}, {n3} sean un par igual!")

print("\nProceso terminado")
