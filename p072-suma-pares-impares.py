## p072-suma-pares-impares.py
## Imprimir números pares e impares, y su suma, el usuario elige

while True:
    print('\033[2J\033[H')

    print("Imprimir números pares o impares y su suma")
    print("[1] Pares")
    print("[2] Impares")
    op= int(input("Elige: "))

    n=int(input("\nLímite?: "))

    s=0

    if op==1:
        print(f"\nImprimiendo números Pares y su suma")
        for i in range(2,n+1,2):
            print(i,end=" ")
            s+=1
        print("\nSuma Pares "+ str(s))
    elif op==2:
        print(f"\nImprimiendo números Impares y su suma")
        for i in range(1,n+1,2):
            print(i,end=" ")
            s+=1
        print("\nSuma Impares "+ str(s))
    else:
        print("\n\nOpción Invalida")
        
    if input("\n\nDeseas continuar (S/N)").upper()=="N": break

print("Proceso Terminado")