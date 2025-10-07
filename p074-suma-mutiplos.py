## p074-suma-mutiplos.py
## Imprime los multiplos m de 1 a n y su suma, usando un ciclo for

while True:
    print('\033[2J\033[H')
    ("Imprimiendo y sumando números")
    n= int(input("Hasta dónde: "))
    m= int(input("Multiplos: "))

    cm=0
    sm=0

    for i in range(1,n+1):
        if i %m==0:
            print(i, end=" ")
            cm+=1
            sm+=1
    print(f"\nFueron {cm} multiplos, que suman {sm}")

    if input("\n\nDeseas continuar (S/N)").upper()=="N": break

print("Proceso Terminado")