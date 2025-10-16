## p097-procesar-datos-sensores.py
## Simular la recolección de datos de 2 sensores

print('\033[2J\033[H')
print("Simular la recolección de datos de 2 sensores.")

import random

max=10
sen_a= []
sen_b= []
todo= []

for _ in range(max):
    sen_a.append(random.randint(1,100))
    sen_b.append(random.randint(1,100))

print(f"\nReporte de lecturas de sensores:")
print(f"Sensor A: {sen_a}")
print(f"Sensor B: {sen_b}")

for i in range(max):
    sen_a[i]= sen_a[i]**2
    sen_b= sen_b[i]**2
    todo.append(sen_a[i]) + sen_b[i]

print(f"\nReporte de lecturas de sensores:")
print(f"Sensor A: {sen_a}")
print(f"Sensor B: {sen_b}")
print(f"Combinando: {todo}")