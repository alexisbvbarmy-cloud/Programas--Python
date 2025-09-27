## p040-calculo-notas.py
## Calculo del promedio de 5 calificaciones calificaciones 

print("\033[2j\033[H")
print("-----Calcular promedio de calificaciones-----")
print("Ingresa 5 calificaciones separadas por un espacio para calcular el promedio:")
n1, n2, n3, n4, n5= input().split()
n1, n2, n3, n4, n5= float(n1), float(n2), float(n3), float(n4), float(n5)
prom= (n1+n2+n3+n4+n5)/5

if prom<6:
    print(f"Tu promedio es: {prom}. Queda Reprobado")
elif prom>6 and prom<7:
    print(f"Tu promedio es: {prom}. Pasa de panzazo")
elif prom>7 and prom<8:
    print(f"Tu promedio es: {prom}. Muy bien, puedes mejorar")
elif prom>8 and prom<9:
    print(f"Tu promedio es: {prom}. Excelente, sigue así")
elif prom>9 and prom<10:
    print(f"Tu promedio es: {prom}. Perfecto, tu esfuerzo valió la pena")


print("\nProceso Terminado")