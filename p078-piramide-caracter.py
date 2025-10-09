## p078-piramide-caracter.py
## 

print('\033[2H\033[J')
print("Imprime una piramide de n renglones de el caracter deseado")

n=int(input("Renglones: "))
m=input("Caracter: ")

# El bucle exterior se ejecuta n veces
for i in range(1,n+1):
    
    espacios=n-i
    for k in range(espacios):
        print(" ", end='')
    
    caracteres=2*i-1
    # Por cada iteración del bucle exterior, el bucle interior se ejecuta m veces
    for j in range(0,caracteres):
        print(f"{m}", end='')
    
    print("\r")