## 071-arriba-abajo.py
## Imprimir números de 1 a n, o de n a 1, segpun elija el usuario, usando el coclo for

while True:
    print('\033[2J\033[H')

    print("Imprimir números usando ciclo for - Arriba o Abajo")
    print("[1] Arriba de 1 a n")
    print("[2] Abajo de n a 1")
    op= int(input("Elige: "))

    n=int(input("\nLímite?: "))

    if op==1:
        print(f"\nImprime números de 1 a {n}")
        for i in range(1,n):
            print(i,end=" ")
        print("\n\n")
    elif op==2:
        print(f"\nImprime números de {n} a 1")
        for i in range(n,0,-1):
            print(i, end=" ")
        print("\n\n")
    else:
        print("\n\nOpción Invalida")
        
    if input("\n\nDeseas continuar (S/N)").upper()=="N": break

print("Proceso Terminado")