## p039-numeros-romanos.py
## Ingresa un número del 1 al 10 para convertirlo en romano.

print("\033[2j\033[H")
print("-----Convertir a números romanos-----")
print("Ingresa un número del 1 al 10 para convertirlo en número romano:")
n1= int(input())

# Proceso 
if n1==1:
    print("I")
elif n1==2:
    print("II")
elif n1==3:
    print("III")
elif n1==4:
    print("IV")
elif n1==5:
    print("V")
elif n1==6:
    print("VI")
elif n1==7:
    print("VII")
elif n1==8:
    print("VIII")
elif n1==9:
    print("IX")
elif n1==10:
    print("X")
else:
    print("Error: Número Invalido")

print("\nProceso Terminado")