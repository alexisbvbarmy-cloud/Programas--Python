## p032-aceptar-estudiante.py
## Aceptar a un estudiante en base a la edad y 2 calificaciones 
## usaremos or

print("\033[2j\033[H")
print("--- Amisión de estudiantes a la Universidad ---")

nombre= input("Dame tu nombre")
edad= int(input("Edad:"))

if edad<18:
    print(f"Lo sentimos {nombre}, sólo aceptamos menores de edad y tu cuentas con {edad} años")
else:
    print("Ingresa 2 calificaciones separadad por ENTER")
    cal1=float(input())
    cal2=float(input())
    if cal1<8 or cal2<8:
        print(f"Lo sentimos, se requierren 2 calificaciones de 8 como mínimo, y tu tienes {cal1} y {cal2}")
    else:
        print(f"Bienvenido {nombre}, tu edad {edad}, y tus calificaciones de {cal1} y {cal2} te permiten entrar")    

print("\nProceso Terminado")
