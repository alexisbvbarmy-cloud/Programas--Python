## p114-area-figuras.py
## Crear una lista de diccionarios para representar figuras geométricas

import math

figuras = {
"Circulo": {"radio": 0, "formula": "math.pi * r ** 2"},
"Triangulo": {"base": 0, "altura": 0, "formula": "0.5 * b * a"},
"Rectangulo": {"largo": 0, "ancho": 0, "formula": "l * a"}
}

print('\033[H\033[J')
print('Área de Figuras Geométricas\n')

print(f"\nFiguras disponibles")
for k, v in figuras.items():
    print(f"{k:<10} - Formula: {v["formula"]}")

while True:
    fig= input("\nElige figura: ").title()
    if fig in figuras: break
    print("X")

area=0

if fig=="Circulo":
    r=float(input("Radio: "))
    area= eval( figuras[fig]["formula"].replace("r",str(r)))
    print(f"Fórmula: {figuras[fig]["formula"]}")
elif fig=="Triangulo":
    b=float(input("Base: "))
    h=float(input("Altura: "))
    area= eval(figuras[fig]["formula"].replace("b",str(b).replace("a",str(h))))
    print(f"Fórmula: {figuras[fig]["formula"]}")
elif fig=="Rectangulo":
    l=float(input("Largo: "))
    a=float(input("Ancho: "))
    area= eval(figuras[fig]["formula"].replace("l",str(l).replace("a",str(a))))
    print(f"Fórmula: {figuras[fig]["formula"]}")

print(f"\nEl área de {fig} que tú elegiste es: {area:.4f}")