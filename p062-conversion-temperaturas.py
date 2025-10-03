## p062-conversion-temperaturas.py
## El usuario debe introducir una temperatura inicial y una final en grados Celsius. El programa mostrará la conversión a grados Fahrenheit para cada grado en ese rango, incrementando de uno en uno.

print("\033[2j\033[H")
print("Conversión de temperatura según el rango que de el usuario")

temp_1=int(input("Introduce una Temperatura inicial en °C: "))
temp_2= int(input("Introduce la temperatura final en °C: "))

if temp_1>temp_2:
    print("La temperatura inicial debe ser menor que la temperatura final")
else:
    print("\nCo0nversión: °C a °F")
    temp=temp_1
    while temp<=temp_2:
        far=(temp*9/5)+32
        print(f"Temperatura: {temp} °C = {far} °F")
        temp+=1
  

