## p042-precio-entrada-cine.py
## Determina el precio de la entrada al cine según la edad del cliente.

print("\033[2j\033[H")
print("-----Calcula el precio de la entrada al cine -----")
edad=int(input("Dime tu edad: "))

# Proceso 
if edad<5:
    print("Tu entrada es gratis")
elif edad>5 and edad<=12:
    print("Tu entrada es a $5")
elif edad>12 and edad<=64:
    print("Tu entrada es a $10")
else:
    print("Tu entrada es a $7")

print("\nProceso Terminado")