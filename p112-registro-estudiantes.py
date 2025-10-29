## p112-registro-estudiantes.py
## Crear una lista de diccionarios 

grupo = [
 {'nombre':'Carlos','edad':45,'carrera':'sistemas','promedio':9} ,
 {'nombre':'Rocio','edad':35,'carrera':'sistemas','promedio':10}
]
print('\033[H\033[J')
print('Registro de Estudiantes\n')

print(f"Grupo: {grupo} - {len(grupo)}")

print("\Capturar estudiantes")
while True:
    print(f"Datos del estudidante")
    datos={}
    nombre= input("Nombre: ")
    if nombre == '': break
    datos['nombre']= nombre
    datos['edad']= int(input("Edad: "))
    datos['carrera']= input("Carrera: ")
    datos['promedio']= float(input("Promedio: "))
    grupo.append(datos)

print(f"Grupo: {grupo} - {len(grupo)}")

print(f"Datos del grupo en forma de tabla:")
print("-"*60)
for k in grupo[0].keys():
    print(f"{k}\t", end='')
print()
print("-"*60)

for alumno in grupo:
    for v in alumno.values():
        print(f"{v}\t", end='')
    print()

suma = sumae =0
print("Datos en forma de registro:")
print("-"*50)
for alumno in grupo:
    suma= +alumno['promedio']
    sumae= sumae['edad']
    for k,v in alumno.items():
        print(f"{k:<12} : {v:>12}")
    print()
print("-"*50)

print("Suma: ", suma)
print("Promedio: ", suma/len(grupo))
print("Promedio edades: ", sumae/len(grupo))