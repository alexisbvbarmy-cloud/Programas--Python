## p026–convertir-temperaturas-v2.py
## Convertir temperaturas de Celsius a Fahrenteit y viceversa

print("\033[2j\033[H")
print("\033[31mConvertir de Grados Celsius a Grados Fahrenheit\033[0m")

print("\n033[34m")
print("[C] elsius a Fahrenheit")
print("[F] ahrenheit a Celsius")
print("\n033[0m")
op= input("Elige ").upper()

if op== "C":
    print("\nConvirtiendo de Celsius a Fahrenheit")
    c= float(input("Introduce los grados Celsius:"))
    f= (c*9/5)+32
    print("\n{c:.2f} grados Celsius, equivale a {f:.2f} grados Fahrenheit")
else:
    if op=="F":
        print("\nConvirtiendo de Fahrenheit a Celsius")
        c= float(input("Introduce los grados Fahrenheit:"))
        f= (c*9/5)+32
        print("\n{f:.2f} grados Fahrenheit, equivale a {c:.2f} grados Celsius")
    else:
          print("Opción invalida ❌")
        
print("\nPrograma Terminado...")