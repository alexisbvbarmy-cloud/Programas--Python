## p052-tabla-conversion.py
## Mostrar una tabla de conersión de peso a dolares 

tc= 20.71

while True: # reíta el proceso las veces que el usuario pida
    print("\033[2j\033[H")
    print("Tabla de conversió de Peso a Dolar")
    print(f"Tipo de cambio: {tc} pesos por dolar")
    print("-"*25)

    while True: # calida los valores inicial y final
        pi= float(input("Valor Inicial: "))
        pf= float(input("Valor Final: "))
        if (pi>0 and pf>0) and (pi<pf): break
        print("Error en lo valores de entrada, intenta de nuevo")

    c= pi
    print("\nPesos\t\tDolar")
    while c<=pf:
        print(f"{c:.2f} \t\t{c/tc:.2f}")
        c+=1

    if input("\nDeseas continuar? [S/N]").upper()=='N': break

print("\nProceso Terminado")