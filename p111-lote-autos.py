## p111-lote-autos.py
## Crear una lista de diccionarios para presentar un conjunto de autos.

autos = [
{ 'marca':'Ford', 'modelo':'Mustang', 'Año': 1964 },
{ 'marca':'VW', 'modelo':'Jetta', 'Año': 2015 }
]


print('\033[H\033[J')
print("Listado de Autos\n")

print(f"Autos: {autos} - {len(autos)}")

autos.append({"Marca":"chevrolet", "Modelo": "Captiva", "Año": 2024})

print(f"Autos: {autos} - {len(autos)}")

print("\nCada auto dentro de los autos:")
for auto in autos:
    print(auto)

print(f"Datos de los autos en forma de tabla:")
print("-"*50)
for k in autos[0].keys():
    print(f"{k}\t", end='')
print()
print("-"*50)

for auto in autos:
    for v in auto.values():
        print(f"{v}\t", end='')
    print()

suma_year=0
print("Datos en forma de registro:")
print("-"*50)
for auto in autos:
    suma_year=suma_year +auto['Año']
    for k,v in auto.items():
        print(f"{k:<12} : {v:>12}")
    print()
print("-"*50)