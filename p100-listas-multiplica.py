## p100-listas-multiplica.py
## Leer dos listas de 5 elementos numéricos, crear una ternera lista multiplicando los elementos de las dos listas corresóndientes

print('\033[2J\033[H')
print("----- Multiplicar dos listas -----")
print("Ingresa 5 números para cada lista")

lista1 = []
print("\n--- Primera Lista ---")
for i in range(5):
    while True:
        try:
            numero = float(input(f"Ingresa el elemento {i+1}: "))
            lista1.append(numero)
            break
        except ValueError:
            print("Error: Por favor ingresa un número válido")

lista2 = []
print("\n--- Segunda Lista ---")
for i in range(5):
    while True:
        try:
            numero = float(input(f"Ingresa el elemento {i+1}: "))
            lista2.append(numero)
            break
        except ValueError:
            print("Error: Por favor ingresa un número válido")

lista3 = []
for i in range(5):
    multiplicacion = lista1[i] * lista2[i]
    lista3.append(multiplicacion)

# Mostrar resultados
print("\n" + "="*50)
print("RESULTADOS:")
print("="*50)
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3 (Multiplicación): {lista3}")
print("\n--- Detalle de Operaciones ---")
for i in range(5):
    print(f"{lista1[i]} × {lista2[i]} = {lista3[i]}")
