## p076-tablas-todas.py
## Imprime todas las tablas de multiplicar desde n hasta m, usando ciclo for 

print('\033[2J\033[H')
print("Imprimiendo las tablas de multiplicar de 1 a n, hasta m")

n=int(input("Hasta qué tabla?: "))
m=int(input("Hasta qupe multiplicador?: "))

# El bucle exterior se ejecuta n veces
for i in range(1,n+1):
    print(f"\n----- Tabla del {i}")

    # Por cada iteración del bucle exterior, el bucle interior se ejecuta m veces
    for j in range(1,m+1):
        print(f"{i} X {j} = {i*j}")
    
    print("\n")
