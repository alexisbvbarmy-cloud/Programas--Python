## p054-tabla-multiplicar-while-v1.py
## Imprime la tabla de T hasta N

while True:
    print("\033[2j\033[H")
    print("Imprime la Tabla de multiplicar T hasta N")

    while True:
        t= int(input("Qué tabla quieres?: "))
        n= int(input("Hasta dónde la quieres?: "))
        if t>0 and n>0:
            break
        print("Error, los números deben ser mayores que 0")

    c=1
    while (c<=n):
        print(f"{t} X {c} = {t*c}")
        c+=1
    
    if input("\nDeseas continuar? [S/N]").upper()=='N': 
        break

print("\n\nGracias por utilizar este programa")