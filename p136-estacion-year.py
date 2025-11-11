## p136-estacion-year.py
#

def estacion(mes:int) -> str:
    est=""
    if mes in (12,1,2):
        est= "Invierno"
    elif mes in (3,4,5):
        est= "Primavera"
    elif mes in (9,10,11):
        est= "Otoño"
    else:
        est="Mes inválido"

    return est

print(f"Es mes 1 corresponde a: {estacion(1)}")
print(f"Es mes 1 corresponde a: {estacion(10)}")

print("dame un número de mes entre 1 y 12")
mes= int(input())
print(f"La estación del año para el mes {mes} es: {estacion(mes)}")