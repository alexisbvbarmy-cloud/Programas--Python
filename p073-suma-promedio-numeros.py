## p073-suma-promedio-numeros.py
## Suma y promedia n números introducidos por el usuario

while True:
    print('\033[2J\033[H')
    ("Sumando y promediando números")

    n= int(input("Cuántas Calificaciones: "))

    s=0
    numeros=""
    for i in range(1, n+1):
        c=int(input(f"Calificación {i}: "))
        s+=c
        numeros += str(c)+ " "
    
    print(f"Las calificaciones fueron: {n}")
    print(f"La suma es: {s}")
    print(f"El Promedio es: {s/n}")


    if input("\n\nDeseas continuar (S/N)").upper()=="N": break

print("Proceso Terminado")