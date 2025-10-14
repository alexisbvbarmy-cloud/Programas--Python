## p089-agregar-lista.py
## Mostrar las diferentes formas para agregar elementos a una lista 

print('\033[2J\033[H')
print("Agregar elementos a una lista")

nums=[80.3, 12.5, 60.2, 30.4]
print(f"Temperaturas iniciales: {nums} - {len(nums)}")

print(f"Agregar los valores: 90 y 100 al final:")
nums.append(90)
nums.append(100)
print(f"Resultado: {nums} - {len(nums)}")

print("Insertar el 80 en la posición 4:")
nums.insert(4, 80)
print(f"Resultado: {nums} - {len(nums)}")

print(f"Extender datos agregando (110, 120, 130) al final ")
nums.extend([110,120,130])
print(f"Resultado: {nums} - {len(nums)}")