## p035-tipo-triangulo.py
## Clasificar un triángulo según la lingitud de sus lados
## lados iguales equilatero, dos lados iguales isoceles, ningún lado igual escaleno

print("\033[2j\033[H")
print("Clasificador de triángulo")

l1= float(input("Lado 1: "))
l2= float(input("Lado 2: "))
l3= float(input("Lado 3: "))

if l1==l2==l3:
    print(f"Es un triángulo Equilatero dado que todos sus lados on iguales")
elif l1==l2 or l1==l3 or l2==l3:
    print(f"Es un triángulo Isoceles debido a que dos de sus lados son iguales")
else: 
    print(f"Es un triángulo Escaleno, debido a que todos sus lados son diferentes")
    
print("\nProceso Terminado")
