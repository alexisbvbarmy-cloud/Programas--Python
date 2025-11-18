## p142-suma-lista.py
## Función que recibe una lista fe flotantes y regresa su suma

from typing import List

def suma_lista(lista:list) -> float:
    suma=0
    for numero in lista:
        suma+=numero
    return suma

numeros= [1.5, 2.3, 3.7, 4.0]
resultado= suma_lista(numeros)
print(f"La suma de los números es {resultado}")

