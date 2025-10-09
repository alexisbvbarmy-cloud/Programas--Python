## p077-triangulo-caracter.py
## Imprime un triágulo rectángulo de n renglones de el caracter deseado

print('\033[2J\033[H')
print("Imprime un triágulo rectángulo de n renglones de el caracter deseado")

n=int(input("Renglones: "))
m=input("Caracter: ")

# El bucle exterior se ejecuta n veces
for i in range(1,n+1):

    # Por cada iteración del bucle exterior, el bucle interior se ejecuta m veces
    for j in range(1,i):
        print(f"{m}", end='')
    
    print("\r")
