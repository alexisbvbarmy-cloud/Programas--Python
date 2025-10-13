## p085-rombo-caracter.py
## Solicitar al usuario un número entero impar n que representará la altura y el ancho del rombo.

print('\033[2J\033[H')
print("=== DIBUJADOR DE ROMBO ===\n")

# Validar número impar
while True:
    try:
        n = int(input("Ingrese un número impar para el tamaño: "))
        if n > 0 and n % 2 == 1:
            break
        else:
            print("Debe ser un número impar positivo.")
    except ValueError:
        print("Ingrese un número válido.")

# Validar carácter
while True:
    c = input("Ingrese el carácter: ")
    if len(c) == 1:
        break
    else:
        print("Ingrese solo un carácter.")

print(f"\nRombo de tamaño {n}:\n")

mitad = n // 2

# Dibujar rombo completo
for i in range(-mitad, mitad + 1):
    espacios = abs(i)
    caracteres = n - 2 * espacios
    
    # Imprimir espacios
    print(" " * espacios, end="")
    
    # Imprimir caracteres
    print((c + " ") * caracteres)