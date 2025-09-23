## p033-aceptar-estudiante-v2.py
## Aceptar a un estudiante
## con and

print("\033[2j\033[H")
print("--- Amisión de estudiantes a la Universidad ---")

nombre= input("Dame tu nombre")
edad= int(input("Edad:"))

if edad>=18:
    print("El proceso continua")
    print("Ingresa 2 calificaciones separadad por ENTER")
    cal1=float(input())
    cal2=float(input())
    if cal1>=8 and cal2>=8:
        print(f"Bienvenido {nombre}, tu edad {edad}, y tus calificaciones de {cal1} y {cal2} te permiten entrar")
    else:
        print(f"Lo sentimos, se requierren 2 calificaciones de 8 como mínimo, y tu tienes {cal1} y {cal2}")    
else:
    print(f"Lo sentimos {nombre}, sólo aceptamos menores de edad y tu cuentas con {edad} años")

print("Proceso Terminado")