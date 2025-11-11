## p134-cuadro-caracter.py

def dibuja_cuadro(ren:int, col:int, car:str) -> None:
    for r in range (ren):
        for c in range(col):
            print(car, end="")
        print("")
    print("")

# Dibuja cuadro (4, 10, "*")
# dicuja cuadro (3, 5, "#")

rem= int(input("Renglones"))
cols = int(input('Ingrese el número de columnas del cuadro: '))
caracter = input('Ingrese el carácter para dibujar el cuadro: ')
dibuja_cuadro(rem, cols, caracter)

# Ejemplo de uso:
dibuja_cuadro(4, 10, '*')
dibuja_cuadro(3, 5, '#')