## p028-retira-cuenta.py
## Simula el retiro de dinero de una cuenta de ahorros, revisa el saldo 

saldo_actual= 15000.00

print("\033[31mSimulacro de retiro de cuenta\033[0m")
print("\033[2j\033[H")
print(f"Tu saldo es: {saldo_actual}")

cantidad_retiro= float(input("Cantidad a retirar: $"))

if cantidad_retiro>0:
    if cantidad_retiro <= saldo_actual:
        print("Procedimiento de retiro...")
        saldo_actual-=cantidad_retiro
        print("\nRetiro exitoso")
        print(f"Tu nuevo saldo es: ${saldo_actual:,.2f}")
    else:
        print("\nFondos Insuficientes para completar la transacci+on")
else:
    print("\nLa cantidad a retirar debe ser un número positivo")

print("\nProceso terminado")