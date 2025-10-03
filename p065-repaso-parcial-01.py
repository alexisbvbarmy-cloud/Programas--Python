## p065-repaso-parcial-01.py
## Objetivo PRograma para calcular las ventas de una papelería 
## Fecha: 02 de octubre de 2025

print("\033[2j\033[H")

ventas= cantidad= subtotal =0
cantidad_c = cantidad_o = cantidad_d = cantidad__p=0
total_c=total_o=total_d=total_p=0
while True:
    ventas+=1
    print(f"\nVenta {ventas}")

    tipo=input("Tipo de copia (C)arta $3, (O)ficio $4, (D)oble Of. $6, (P)lano $12?: ").upper()

    if tipo not in 'CODP':
        err=input(">>>Error.Tipo de copia noo válido. Intente de nuevo. <ENTER>")
        vetnas-=1
        continue

    cantidad=int(input("Cantidad: ")) 
    descuento= 1
    if cantidad >50:
        descuento=0.90
        print("**Descuento del 10% aplicado por volumen de venta**")

    if tipo=='C':
        cantidad_c += cantidad
        subtotal=(cantidad*3)*descuento
        total_c+=subtotal
    elif tipo=='O':
        cantidad_o += cantidad
        subtotal=(cantidad*4)*descuento
        total_o+=subtotal
    elif tipo=='D':
        cantidad_d += cantidad
        subtotal=(cantidad*6)*descuento
        total_d+=subtotal
    elif tipo=='P':
        cantidad__p += cantidad
        subtotal=(cantidad*12)*descuento
        total_p+=subtotal

    if input("Otra venta (S/N)?: ").upper() !='S':break

total_copias= cantidad_c+cantidad_o+cantidad_d+cantidad__p
total_ventas= total_c+total_o+total_d+total_p

print("\n---------------------------------")
print("Resumen de ventas")
print("\n---------------------------------")
print(f"Ventas Realizadas {ventas}")
print("\n---------------------------------")
print(f"Carta\t\t: {cantidad_c:2d} - ${total_c:8.3f}")
print(f"Oficio\t\t: {cantidad_o:2d} - ${total_o:8.3f}")
print(f"Doble Oficio\t: {cantidad_d:2d} - ${total_d:8.3f}")
print(f"Plano\t\t: {cantidad__p:2d} - ${total_p:8.3f}")
print("\n---------------------------------")
print(f"Total Copias\t: {total_copias:2d} - ${total_ventas:8.3f}")

mensaje_venta=""
if total_ventas>150:
    mensaje_venta="Venta Superada"
elif total_ventas>=50:
    mensaje_venta="Venta Frecuente"
else:
    mensaje_venta="Venta Moderada"

print(f"Esta es una: {mensaje_venta}")
print("\nFin de las ventas por este día")