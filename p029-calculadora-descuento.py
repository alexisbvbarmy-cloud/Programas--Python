## p029-calculadora-descuento.py
## Simula una calculadora de descuentos con base en el monto de compra

compra=descuento=porcentaje=total=0.0

print("\033[2j\033[H")
print("\033[31mCalculadora de Descuentos\033[0m")

compra=float(input("Ingresa el total de la compra: $"))

if compra>2000:
    porcentaje=0.20
else:
    if compra>1000:
        porcentaje=0.10
    else:
        if compra>500:
            porcentaje=0.05
        else:
            porcentaje= 0

descuento=compra*porcentaje
total=compra-descuento

print("Resumen Final")
print(f"Total de la compra: {compra}")
print(f"Porcentaje de descuento: {porcentaje:.5f}")
print(f"Descuento: {descuento:.5f}")
print(f"Total a pagar: {total:.5f}")

print("Proceso Terminado")