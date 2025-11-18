## p146-pares-impares.py
## Funcion que retorna los pares e impares de una lista

from typing import List; tuple

def lista_pares_impares(lista:List[int]) -> tuple[List[int], List[int]]:
    pares : List[int]= []
    impares: List[int]= []
    for numero in lista:
        if numero % 2 ==0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

numeros: List[int] = [1,2,3,4,5,6,7,8,9,1, 11, 12, 13]
pares, impares = lista_pares_impares(numeros)

print(f"Lista números: {numeros} - {len(numeros)}")
print(f"Lista pares: {pares} - {len(pares)}")
print(f"Lista impares: {impares} - {len(impares)}")