## p041-aceptar-estudiante-v2
## Ingreso a "Universidad Kitty Kat SA"
## Requisitos para ingreso: ser mayor de 21 años, ser mujer y tener un promedio entre 8 y 9.5

print("\033[2j\033[H")
print("-----Ingreso a ´Universidad Kitty Kat SA´-----")
print("Ingresa los datos  y 3 calificaciones de la estudiante:")
nombre=input("Nombre: ")
nombre= str(nombre)
sexo=input("Sexo. Teclear H o M mayúscula: ")
sexo= str(sexo)
edad=input("Edad: ")
edad=int(edad)
print("Calificaciones separadas por un espacio")
c1, c2, c3= input().split()
c1, c2, c3= float(c1), float(c2), float(c3)
prom= (c1+c2+c3)/3
 
# Proceso 
if sexo=="H":
    print(f"Lo sentimos {nombre}, sólo aceptamos mujeres en esta institución")
elif edad<21:
    print(f"Lo sentimos {nombre}, no cumples con la edad suficiente para el ingreso")
elif prom<8:
    print(f"Lo sentimos {nombre}, tu promedio de {prom:.2f} no es suficiente para cubrir el requisito de ingreso")
else:
    print(f"Felicidades {nombre}, tu edad de {edad} años y tu promedio de {prom:.2f} cumplen con los requisitos de ingreso")

print("\nProceso Terminado")
