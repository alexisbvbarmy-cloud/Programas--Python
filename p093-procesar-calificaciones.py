## p093-procesar-calificaciones.py
## Procesar las calificaciones de un alumno, usando listas. 

print('\033[2J\033[H')
print("Procesar las calificaciones de un alumno")

califs= ()
suma=0.0

while True:
    try:
        cal= float(input("Calificación: "))
        if cal==99: break
        if 0 <= cal <= 10:
            califs.append(cal)
            suma+=cal
        else:
            print("Calificación no válida")
            
    except:
        print("Error: Entrada no válida.")

    if not califs:
        print("No se capturaron calificaiones")
    else:
        prom= sum(califs)/len(califs)
        mayor_prom= []
        for cal in califs:
            if cal > prom:
                mayor_prom.append(cal)

print(f"Se capturaron {len(califs)} calificaciones")
print(f"Las calificaciones fueron {califs}")
print(f"\nEstadísticas del curso.")
print(f"Suma: {suma}")
print(f"Promedio: {prom}")
print(f"Calificaciones mayores al promedio: {len(mayor_prom)} -> {mayor_prom}")
print(f"Valificación más alta: {max(califs)}")
print(f"Valificación más baja: {min(califs)}")