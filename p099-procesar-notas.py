## p099-procesar-notas.py
## Leer y procesar un número indeterminado de calificaciones entre 0 y 100,
## Se detiene cuando el usuario introduce O,
## Validar que todas las notas introducidas estén dentro del rango [0,100],
## 

print('\033[2J\033[H')
print("----- Procesar Notas -----")

califs= []
suma=0.0

while True:
    try:
        cal= float(input("Introduce nota de 0 a 100 (0 para detener): "))
        if cal==0: break
        if 0 <= cal <= 100:
            califs.append(cal)
            suma+=cal
        else:
            print("Calificación no válida")
            
    except:
        print("Error: Entrada no válida.")

if not califs:
    print("No se capturaron calificaciones")
else:
    prom= suma/len(califs)
    mayor_prom= []
    men_prom= []
    for cal in califs:
        if cal > prom:
            mayor_prom.append(cal)
        elif cal<prom:
            men_prom.append(cal)


print("\n--> Resultados <---")
print(f"Total de notas: {len(califs)}")
print(f"Lista de notas: {califs}")
print(f"Suma de notas: {suma}")
print(f"Promedio de notas: {prom:.2f}")
print(f"Nota máxima: {max(califs)}")
print(f"Nota mínima: {min(califs)}")
print(f"Cantidad de notas menores al promedio: {len(men_prom)}")
print(f"Notas menores al promedio: {men_prom}")