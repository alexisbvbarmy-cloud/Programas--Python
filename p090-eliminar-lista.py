## p090-eliminar-lista.py
## Mostrar cómo eliminar elementos de una lista

print('\033[2J\033[H')
print("Eliminar elementos de una lista")

nums=[1,3,5,7,9,11,99,15,88,19,100]

print(f"Datos originales con anomalías: {nums} - {len(nums)}")

print(f"Elminar el valor 99:")
nums.remove==99
print(f"Resultado: {nums} - {len(nums)}")

print(f"Eliminar el elemento de la posición 8:")
num_rem=nums.pop(8)
print(f"Resultado: {nums} - {len(nums)} - Se removío: {num_rem}")

print(f"Eliminar el último elemento:")
num_rem=nums.pop()
print(f"Resultado: {nums} - {len(nums)} - Se removío: {num_rem}")

print(f"Eliminasr todas la mediciones:")
nums.clear()
print(f"Resultado: {nums} - {len(nums)}")