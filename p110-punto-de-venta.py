## p110-punto-de-venta.py
## Simulación de un punto de venta usando diccionarios

print('\033[H\033[J')
print('Simulación de un punto de venta usando diccionarios\n')

menu = {
'taco': 18.50,
'burrito': 45.00,
'quesadilla': 35.00,
'refresco': 20.00,
'agua': 15.00
}

print("\n------ Bienvenido --------")
print("Este es nuestro menú: ")
for a, p in menu.items():
    print(f"- {a:<12}: ${p:,.2f}")

orden={}
total_general=0


while True:
    producto= input("Qué deseas: ").lower()
    if producto=='fin': break
    cantidad= int(input("Cantidad: "))
    orden[producto]= orden.get(producto,0) + cantidad
    print(f"Agregados: {cantidad} {producto} a tu orden.")

print(f"Tu orde fue: \n{orden}")

print(f"\n------Recibo de pago -------")
if not orden:
    print("No compraste nada")
else:
    for p,c in orden.items():
        precio_unitario=menu[p]
        subtotal= precio_unitario*cantidad
        print(f"{c} X {p:<12}: ${subtotal:,.2f}")

print('-'*35)
print(f"Total a pagar: ${total_general:,.2f}")
print("Gracias por tu compra!!")