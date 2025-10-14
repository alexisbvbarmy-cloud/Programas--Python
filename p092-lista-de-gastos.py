## p092-lista-de-gastos.py
## Permite llevar el control de una lista de gastos

print('\033[2J\033[H')
print("Iterar elementos de una lista")

gastos=[450.50, 120.00, 85.90, 230.00, 55.75]
limite_gasto=100.00

while True:
    print("\n----- Menú de gestión de gastos -----")
    print("1.- Ver todos los gastos")
    print("2.- Agregar un nuevo gasto")
    print("3.- Modificar un gasto existente")
    print("4.- Eliminar un gasto (por reembolso o error)")
    print("5.- Ver resumen y total de gastos")
    print("6.- Salir")
    opcion=int(input("Elige una opción (1-6): "))

    if opcion==1: 
        print("\n----- Tus gastos registrados -----")
        print(gastos)
    elif opcion==2:
        try:
            nuevo_gasto= float(input("Ingresa el monto del nuevo gasto: "))
            gastos.append(nuevo_gasto)
            print(f"Gasto de $: {nuevo_gasto:.2f} agregado correctamente.")
        except ValueError:
            print("Error: por favor, ingresa un número válido.")
    elif opcion==3:
        try:
            pos=int(input("Ingresa la posición en la lista del gasto que quieres modificar: "))
            valor_anterior=gastos[pos]
            print(f"Gasto a modificar gastos [{pos}] ${valor_anterior:.2f} ")
            nuevo_valor= float(input("Ingresa el nuevo monto del gasto: "))
            gastos[pos]=nuevo_valor
            print(f"Gasto modificado de ${valor_anterior:.2f} a ${nuevo_valor:.2f}")
        except ValueError:
            print("Error: Por favor, ingresa un número válido")
    elif opcion==4:
        try:
            gasto_a_eliminar= float(input("Ingresa el monto del gasto que quieres eliminar: "))
            if gasto_a_eliminar in gastos:
                gastos.remove(gasto_a_eliminar)
                print(f"Gasto de ${gasto_a_eliminar} eliminado correctamente")
            else:
                print("Error. El gasto especificado no se encuentra en la lista.")
        except ValueError:
            print("Error: Por favor, ingresa un número válido")
    elif opcion==5:
        if not gastos:
            print("\nNo hay gastos para mostrar.")
        else:
            total_gastado=0
            print("\n----- Resumen del mes -----")
            for gasto in gastos:
                total_gastado+=gasto
                if gasto>limite_gasto:
                    print(f"Gasto considerable detectrado: ${gasto:.2f}")
                print(f"\nEl gasto total del mes es: ${total_gastado:.2f}")
    elif opcion==6: 
        print("\nGracias por usar el gestor de gastos. Hasta Pronto!") 
        break
    else: 
        print("Opción no válida, introduce un número del 1 al 6.")