## p082-compara-rendimiento-inversion.py
## Compara el crecimiento de de dos fondos de inversión a lo largo de varios años. 
## El usuario ingresa: Monto inicial, Tasa de interés(%) para cada uno, Número de años

print('\033[2J\033[H')
def comparar_fondos_inversion():
    # Solicitar datos al usuario
    print("=== COMPARADOR DE FONDOS DE INVERSIÓN ===\n")
    
    # Datos del Fondo 1
    print("FONDO 1:")
    monto_inicial_1 = float(input("Ingrese el monto inicial: $"))
    tasa_interes_1 = float(input("Ingrese la tasa de interés anual (%): "))
    
    # Datos del Fondo 2
    print("\nFONDO 2:")
    monto_inicial_2 = float(input("Ingrese el monto inicial: $"))
    tasa_interes_2 = float(input("Ingrese la tasa de interés anual (%): "))
    
    # Número de años
    while True:
        try:
            años = int(input("\nIngrese el número de años a proyectar: "))
            if años > 0:
                break
            else:
                print("Por favor, ingrese un número mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    # Inicializar variables
    saldo_1 = monto_inicial_1
    saldo_2 = monto_inicial_2
    año_actual = 1
    
    # Encabezado de la tabla
    print("\n" + "="*70)
    print(f"{'Año':<6} {'Fondo 1 ($)':<15} {'Fondo 2 ($)':<15} {'Diferencia ($)':<15} {'Mayor Rendimiento'}")
    print("="*70)
    
    # Calcular y mostrar el crecimiento anual usando for
    for año in range(1, años + 1):
        # Calcular interés compuesto para cada fondo
        saldo_1 = saldo_1 * (1 + tasa_interes_1 / 100)
        saldo_2 = saldo_2 * (1 + tasa_interes_2 / 100)
        
        # Calcular diferencia
        diferencia = abs(saldo_1 - saldo_2)
        
        # Determinar qué fondo tiene mayor rendimiento
        if saldo_1 > saldo_2:
            mayor_rendimiento = "Fondo 1"
        elif saldo_2 > saldo_1:
            mayor_rendimiento = "Fondo 2"
        else:
            mayor_rendimiento = "Iguales"
        
        # Mostrar resultados del año actual
        print(f"{año:<6} ${saldo_1:<13.2f} ${saldo_2:<13.2f} ${diferencia:<13.2f} {mayor_rendimiento}")
    
    print("="*70)
    
    # Resultados finales
    print("\n=== RESULTADOS FINALES ===")
    print(f"Fondo 1: ${saldo_1:.2f}")
    print(f"Fondo 2: ${saldo_2:.2f}")
    
    # Determinar el fondo ganador usando if-else
    if saldo_1 > saldo_2:
        diferencia_final = saldo_1 - saldo_2
        print(f"\n¡El FONDO 1 es más rentable!")
        print(f"Ventaja sobre Fondo 2: ${diferencia_final:.2f}")
        print(f"Rentabilidad adicional: {(diferencia_final/saldo_2)*100:.2f}%")
        
    elif saldo_2 > saldo_1:
        diferencia_final = saldo_2 - saldo_1
        print(f"\n¡El FONDO 2 es más rentable!")
        print(f"Ventaja sobre Fondo 1: ${diferencia_final:.2f}")
        print(f"Rentabilidad adicional: {(diferencia_final/saldo_1)*100:.2f}%")
        
    else:
        print(f"\n¡Ambos fondos tienen el mismo rendimiento final!")
        print(f"Monto final: ${saldo_1:.2f}")

# Función principal con menú usando while
def main():
    while True:
        print("\n" + "="*50)
        print("    COMPARADOR DE FONDOS DE INVERSIÓN")
        print("="*50)
        
        # Ejecutar la comparación
        comparar_fondos_inversion()
        
        # Preguntar si desea realizar otra comparación
        while True:
            continuar = input("\n¿Desea realizar otra comparación? (s/n): ").lower()
            if continuar in ['s', 'n', 'si', 'no']:
                break
            else:
                print("Por favor, ingrese 's' para sí o 'n' para no.")
        
        if continuar == 'n' or continuar == 'no':
            print("\n¡Gracias por usar el comparador de fondos!")
            break

# Ejecutar el programa
if __name__ == "__main__":
    main()