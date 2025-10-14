## p091-iterar-lista.py
## Mostrar las diferentes formas de iterar por todos los elementos de una lista

print('\033[2J\033[H')
print("Iterar elementos de una lista")

nums=[2,4,6,8,10,12,14,16]

print(f"Todos los números: {nums} - {len(nums)}")

print("\n\n1.- Iteración por elemento:")
for n in nums:
    print(n, end=" ")

print("\n\n2.- Iteración por el índice de cada elemento:")
for i in range(len(nums)):
    print(nums[i], end=" ")

print(f"\n\n3.- Iterar por cada elemento y sumar 2:")
for n in nums:
    print(n+2, end=" ")

print(f"\n\n4.- Iterar por índice y sumar 10:")
for n in nums:
    print(n+10, end=" ")

print(f"\n\n5.- Iteración con enumerate:")
for i, n in enumerate(nums):
    print(i, '\t', n)

print(f"\n\nResultado: {nums} - {len(nums)}")

for n in nums:
    nums[i]=nums[i] *+2
print(f"\n\nModificar la lista al iterar:")
print(f"\n\nResultado: {nums} - {len(nums)}")