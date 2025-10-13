## p083-plan-ahorro-depistos-mensuales.py
## Simulador de un plan de ahorro 
## El usuario ingresa el monto inicial, deposito mensual fijo, tasa de interés mensual (%), y el número total de meses 

print('\033[2J\033[H')
def simulador_plan_ahorro():
    # Solicitar datos al usuario
    print("=== SIMULADOR DE PLAN DE AHORRO ===\n")
    
    # Validar monto inicial
    while True:
        try:
            monto_inicial = float(input("Ingrese el monto inicial: $"))
            if monto_inicial >= 0:
                break
            else:
                print("El monto inicial no puede ser negativo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    # Validar depósito mensual
    while True:
        try:
            deposito_mensual = float(input("Ingrese el depósito mensual fijo: $"))
            if deposito_mensual >= 0:
                break
            else:
                print("El depósito mensual no puede ser negativo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    # Validar tasa de interés mensual
    while True:
        try:
            tasa_interes_mensual = float(input("Ingrese la tasa de interés mensual (%): "))
            if tasa_interes_mensual >= 0:
                break
            else:
                print("La tasa de interés no puede ser negativa.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    # Validar número de meses
    while True:
        try:
            meses_totales = int(input("Ingrese el número total de meses del plan: "))
            if meses_totales > 0:
                break
            else:
                print("El número de meses debe ser mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
    
    # Inicializar variables
    saldo_actual = monto_inicial
    total_intereses = 0
    total_depositado = monto_inicial
    
    # Encabezado de la tabla
    print("\n" + "="*85)
    print(f"{'Mes':<6} {'Saldo Inicial ($)':<18} {'Interés Ganado ($)':<18} {'Depósito ($)':<14} {'Saldo Final ($)':<16}")
    print("="*85)
    
    # Simular cada mes usando for
    for mes in range(1, meses_totales + 1):
        saldo_inicial_mes = saldo_actual
        
        # Calcular interés sobre el saldo inicial (antes del depósito)
        interes_ganado = saldo_inicial_mes * (tasa_interes_mensual / 100)
        
        # Actualizar saldo con interés y depósito
        saldo_final_mes = saldo_inicial_mes + interes_ganado + deposito_mensual
        
        # Mostrar información del mes
        print(f"{mes:<6} ${saldo_inicial_mes:<16.2f} ${interes_ganado:<16.2f} ${deposito_mensual:<12.2f} ${saldo_final_mes:<14.2f}")
        
        # Actualizar acumuladores
        total_intereses += interes_ganado
        total_depositado += deposito_mensual
        saldo_actual = saldo_final_mes
    
    print("="*85)
    
    # Mostrar resumen final
    print("\n=== RESUMEN FINAL DEL PLAN DE AHORRO ===")
    print(f"Saldo final: ${saldo_actual:.2f}")
    print(f"Total depositado: ${total_depositado:.2f}")
    print(f"Total de intereses ganados: ${total_intereses:.2f}")
    print(f"Rendimiento sobre lo depositado: {(total_intereses/total_depositado)*100:.2f}%")
    
    # Análisis adicional usando if-else
    if total_intereses > 0:
        print(f"\n¡Excelente! Tu dinero ha generado ${total_intereses:.2f} en intereses.")
        if (total_intereses/total_depositado)*100 > 10:
            print("Tu plan de ahorro tiene un rendimiento muy favorable.")
        else:
            print("Tu plan de ahorro está generando rendimientos moderados.")
    else:
        print("\nTu plan de ahorro no ha generado intereses.")

# Función principal con menú usando while
def main():
    while True:
        print("\n" + "="*50)
        print("    SIMULADOR DE PLAN DE AHORRO")
        print("="*50)
        print("1. Iniciar nueva simulación")
        print("2. Salir")
        print("="*50)
        
        # Validar opción del menú
        while True:
            try:
                opcion = int(input("Seleccione una opción (1-2): "))
                if opcion in [1, 2]:
                    break
                else:
                    print("Por favor, ingrese 1 o 2.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        if opcion == 1:
            simulador_plan_ahorro()
        else:
            print("\n¡Gracias por usar el simulador de plan de ahorro!")
            break

# Ejecutar el programa
if __name__ == "__main__":
    main()