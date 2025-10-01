## p057-interes-simple.py
## Calcular lo a{os necesarios para alcanzar una meta de ahorro con un +interes simple

while True:
    print("\033[2j\033[H")
    print("Calculadora de años para meta de ahorro con ínteres simple")
    print("-"*60)

    
    cap_1= float(input("Capital Inicial: "))
    tasa_a= float(input("Tasa de ínteres anual: "))
    meta= float(input("Meta de ahorro: "))
    
    cap_2=cap_1
    years=0
    int_anual= cap_1+(tasa_a/100)

    while cap_2 <= meta:
        cap_2+=int_anual
        years+=1
    
    print("-"*60)
    print(f"Para alcanzar la meta de {meta}, necesitas {years} años")
    print(f"El capital actual es: $ {cap_2}")
    
    if input("\nDeseas continuar? [S/N]").upper()=='N': break

print("\nProceso Terminado")