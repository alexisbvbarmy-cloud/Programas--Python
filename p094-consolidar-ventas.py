## p094-consolidar-ventas.py
## Consolidar las ventas de dos sucursales, las ventas las captura el usuario

print('\033[2J\033[H')
print("Consolidar las ventas de dos sucursales.")

ventas= int(input("Cu+antas ventas por sucursal?: "))

ventas1= []
ventas2= []
todo= []

print("\nDame las ventas de la primera sucursal")
for i in range(ventas):
    venta=int(input(f"Vetna de día {i+1}"))
    ventas1.append(venta)

print("\nDame las ventas de la segunda sucursal")
for i in range(ventas):
    venta=int(input(f"Vetna de día {i+1}"))
    ventas2.append(venta)

print("Consolidando las ventas")
for i in range(ventas):
    sumdia= ventas1(i) + ventas2(i)
    todo.append(sumdia)

print("\nReporte de ventas:")
print(f"Sucursal 1: {ventas1}")
print(f"Sucursal 2: {ventas2}")
print(f"Consolidando: {todo}")