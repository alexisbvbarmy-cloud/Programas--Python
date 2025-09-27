## p043-calculadora-anio-bisiesto.py
## Determina si un año ingresado por el usuario es bisiesto.
## es divisible por 4, pero no divisible por 100, a menos que sea divisible por 400


print("\033[2j\033[H")
print("-----Calculadora de año bisiesto-----")
year=int(input("Dame el año: "))

if year%4==0 and year%100!=0 or year%400==0:
    print("El año es bisiesto")
else: 
    print("El año NO es bisiesto")

print("\nProceso Terminado")