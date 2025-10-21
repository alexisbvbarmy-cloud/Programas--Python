# p109-conversion-divisas.py
# Conversor de divisas a pesos mexicanos usando diccionarios

conv = {
'USD': 20.50,
'EUR': 22.30,
'GBP': 25.80,
'JPY': 0.19,
'CAD': 16.20
}

print('\033[H\033[J')
print("Conversor de monedas a pesos mexicanos (MXN)")

print(f"\nOpciones de cambio de moneda a pesos mexicanos MXN")
for m in conv:
    print(f"- {m}")

while True:
    moneda= input("\nIngresa la moneda a convertir: ").upper()
    if moneda in conv: break
    continue

while True:
    try:
        cant= float(input("Ingresa la cantidad en {moneda}: "))
    except ValueError:
        print("Entrada no válida")

res= cant*conv[moneda]
print(f"{cant:,.2f} {moneda} equivale a {res:,.2f} MXN")