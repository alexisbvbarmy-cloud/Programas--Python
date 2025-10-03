## p060-promedio-suma.py
## Leer números introducidos por el usuario hasta que ingrese un 0, mostrar el conteo total de números, la suma y el promedio de la serie

print("\033[2j\033[H")
print("Promedio y suma")

c=0
suma=0

while True:
    num=int(input("Ingresa números (0 para terminar): "))

    if num==0:
        break
    else:
        c+=1
        suma+=num

if c>0:
    promedio=suma/c
else:
    promedio=0

print("\nResultados")
print(f"Cantidad de números ingresados: {c}")
print(f"Suma total= {suma}")
print(f"Promedio: {promedio}")


