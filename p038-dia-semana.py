## p038-dia-semana.py
## Determina el día de la semana a partir de un número dado por el usuario del 1 al 7 

print("\033[2j\033[H")
print("-----Determinar el día de la semana-----")
print("Ingresa un número del 1 al 7 para mostrar el dpia de la semana:")
n1= int(input())

# Proceso 
if n1==1:
    print("Domingo")
elif n1==2:
    print("Lunes")
elif n1==3:
    print("Martes")
elif n1==4:
    print("Miercoles")
elif n1==5:
    print("Jueves")
elif n1==6:
    print("Viernes")
elif n1==7:
    print("Sabado")
else:
    print("Error: Día Invalido")

print("\nProceso Terminado")