## p087-acceder-lista.py
## Acceder a los elementos de una lista por su índice

print('\033[2J\033[H')
nums=[10, 20, 30, 40, 50, 60, 70, 10, 20, 99]

print("Acceder a los elementos de una lista")

print("\nLongitud y contenido")
print(f"Cuántas mediciones son?: {len(nums)}")
print(f"Todas las mediciones: {nums}")

print("\nPrimera y última medición por índice positivo")
print(f"La primera: {nums[0]}")
print(f"La última: {nums[9]}")

print("\nPrimera y última medición por índice negativo")
print(f"La primera: {nums[-10]}")
print(f"La última: {nums[-1]}")

print("\nPor rango")
print(f"Las mediciones de la 2 a la 6: {nums[2:6]}")

print("\nPor sltos consecutivos")
print(f"Las primeras 3 mediciones iniciando de la izquierda: {nums[:3]}")
print(f"Las últimas 3 mediciones, desde la 6 hasta el final: {nums[6:]}")
