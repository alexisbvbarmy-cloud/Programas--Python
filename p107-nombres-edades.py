## p107-nombres-edades.py
##Gestión de nombres y edades usando diccionarios

print('\033[H\033[J')
print('Gestión de nombres y edades usando diccionarios\n')

datos= {}

print("Introduce nombres y edades (nombre vacío para terminar)")

while True:
    nombre= input("Dame el nombre: ")
    if nombre=='': break
    datos[nombre]= int(input("Edad: "))

print(f"\nCenso de Nombres y edades: {datos} - {len(datos)}")

s=0
for n,e in datos:
    print(f"{n:<20} - {e:2}")
    s=s+e

print(f"La suma es: {s}, el promedio es: {s(len(datos)):.2f}")