## p055-tabla-multiplicar-while-v2.py
## Imprime todas las tablas de multiplicar desde la 1 hasta la n, desde el 1 hasta m

while True:
    print("\033[2j\033[H")
    print("Tablas de Multiplicar")

    while True:
        n= int(input("Hasta qué tabla quieres?: "))
        m= int(input("Hasta dónde la quieres?: "))
        if n>0 and m>0:
            break
        print("Error, los números deben ser mayores que 0")

    t=1
    while t<=n:
        c=1
        print(f"\nTabla de {t}\n")
        while (c<=m):
            print(f"{t} X {c} = {t*c}")
        c+=1

    if input("\nDeseas continuar? [S/N]").upper()=='N': 
        break

print("\n\nGracias por utilizar este programa")