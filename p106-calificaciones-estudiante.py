## p106-calificaciones-estudiante.py
## Gestión de calificaciones de un estudiante usando diccionarios

print('\033[H\033[J')
print('Gestión de calificaciones de un estudiante usando diccionarios')

materias= ['física', 'química', 'matemáticas','geografía', 'estadística']
califs= [10,9,8,7.5,6]

print(f"Lista de materias: \n\n{materias}")
print(f"Lista de calificaciones: \n{califs}")

notas= dict(zip(materias, califs))

print(f"\nLas notas: {notas} - {len(notas)}")

notas.update({'ingles':10, 'Programación':7})

print(f"\nLas notas: {notas} - {len(notas)}")

notas.pop('física')
notas.popitem()
print(f"\nLas notas: {notas} - {len(notas)}")

notas.update({'química':10, 'matemáticas':10})
print(f"\nLas notas: {notas} - {len(notas)}")

s=0
print("\nMaterias y calificacionies finales")
for m, c in notas.items():
    print(f"{m:<12} - {c:>5,.2f}")
    s= s+c

print(f"\nLa suma es: {s}")
print(f"\nEl promedio es: {s/len(notas)}")

notas.clear()
print(f"\nLas notas: {notas} - {len(notas)}")