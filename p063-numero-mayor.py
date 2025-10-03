## p063-numero-mayor.py
## Leer una serie de números hasta que el usuario ingrese un 0. Al terminar, el programa deberá mostrar cuál fue el número más grande de todos los introducidos.

print("\033[2j\033[H")
print("Descubrir el número mayor")
print("Ingresa números, 0 para terminar")

mayor=None

num=int(input("Ingresa números: "))
while num!=0:
    if mayor is None:
        mayor=num
    else:
        if num>mayor:
            mayor= num
    num=int(input("Número: "))

if mayor is None:
    print("No se ingresaro números")
else:
    print(f"El número mayor es: {mayor}")