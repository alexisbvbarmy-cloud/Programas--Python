## p080-combina-colores.py
## Genera las combinaciones posibles entre colores

print('\033[2J\033[H')
print("Combinaciones posibles de varios colores")

colores= input("Colores separados por coma").strip().split(',')

for col1 in colores:
    for col2 in colores:
        if col1!=col2:
         print(f"{col1} - {col2}")