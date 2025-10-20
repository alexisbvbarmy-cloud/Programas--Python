## p104-lista-impares.py
## Leer un entero n. Llenar una lista con los primeros n númeors impares.
## Calcular e imprimir: suma y peomedio de los números, números dividibles entre 3 y su suma
## Pedir un elemento a buscar en la lista original e indicar si está y en qué posición. 

print('\033[2J\033[H')
print("Generador de números")

while True:
    try:
        n = int(input("Introduce un número entero n: "))
        if n > 0:
            break
        print("Error: n debe ser positivo")
    except ValueError:
        print("Error: Introduce un número válido")

numeros_impares = []
for i in range(n):
    numeros_impares.append(2 * i + 1)

print(f"\nLista de los primeros {n} números impares:")
print(numeros_impares)

suma_total = sum(numeros_impares)
promedio = suma_total / n

print("\n" + "="*50)
print("RESULTADOS:")
print("="*50)

print(f"1. Suma y promedio:")
print(f"   • Suma total: {suma_total}")
print(f"   • Promedio: {promedio:.2f}")

divisibles_3 = [num for num in numeros_impares if num % 3 == 0]
suma_divisibles_3 = sum(divisibles_3)

print(f"\n2. Números divisibles entre 3:")
if divisibles_3:
    print(f"   • Números: {divisibles_3}")
    print(f"   • Suma: {suma_divisibles_3}")
    print(f"   • Cantidad: {len(divisibles_3)}")
else:
    print("   No hay números divisibles entre 3")

print(f"\n3. Buscar elemento:")
while True:
    try:
        elemento_buscar = int(input("   Introduce el número a buscar: "))
        break
    except ValueError:
        print("   Error: Introduce un número válido")

if elemento_buscar in numeros_impares:
    posiciones = [i for i, num in enumerate(numeros_impares) if num == elemento_buscar]
    print(f"   ✓ El número {elemento_buscar} SÍ está en la lista")
    print(f"   ✓ Posición(es): {posiciones}")
    print(f"   ✓ Primera aparición: índice {posiciones[0]}")
else:
    print(f"   ✗ El número {elemento_buscar} NO está en la lista")