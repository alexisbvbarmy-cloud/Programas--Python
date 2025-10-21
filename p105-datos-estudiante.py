## p105-datos-estudiante.py
## Gestión de datos de estudiantes usando diccionarios

print('\033[H\033[J')
print('Gestión de datos de estudiantes')

estudiante= {
    'nombre':'Juan Perez',
    'edad': '45',
    'email': 'juanperez@mail.com',
    'carrera': 'sistemas'
}

print(f"\nLos datos del estudiante son: \n\n {estudiante}")

estudiante['calificación']=9.5
estudiante['email']='juanp@gmail.com'
print(f"\nLos datos del estudiante son: \n\n {estudiante}")

print("\nIteras por las llaves:")
for k in estudiante.keys():
    print(k)

print("\nIterar por los valores")
for v in estudiante.values():
    print(v)

print("\Iterar por los elementos (ítems)")
for k,v, in estudiante.items():
    print(f"{k:<15}: {v}")