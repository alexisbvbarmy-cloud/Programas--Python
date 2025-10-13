## p084-cuadro-hueco-caracter.py
## Cuadro Hueco Caracter

print('\033[2J\033[H')
print("Imprime un cuadrado hueco de n renglones de el caracter deseado")

# Solicitar datos
lado = int(input("Ingrese el tamaño del lado: "))
caracter = input("Ingrese el carácter: ")

print(f"\nCuadrado hueco de {lado}x{lado}:\n")

# Dibujar el cuadrado
for i in range(lado):
    for j in range(lado):
        if i == 0 or i == lado-1 or j == 0 or j == lado-1:
            print(caracter, end=" ")
        else:
            print(" ", end=" ")
    print()