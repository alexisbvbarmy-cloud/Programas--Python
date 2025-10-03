## p061-suma-200.py
## Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200. Al terminar, mostrar cuántos números se introdujeron a la suma final

print("\033[2j\033[H")
print("Lee números y sumalos hasta que den como resultado 200")

suma=0
c=0

print("Ingresa los números. El programa terminará cuando la suma sea igual a 200")

while suma<200:
    num=int(input("Número: "))
    suma+=num
    c+=1

print("\nResultados")
print(f"Cantidadde números ingresados: {c}")
print(f"Suma Total: {suma}")