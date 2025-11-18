## p147-aleatorios.py
## Genera dos lista con números aleatorios y los suma en una tercera

import random 
from typing import List

def gen_rand(n:int, min:int, max:int) -> List[int]:
    nums:List[int]=[]
    for _ in range (n):
        num=random.randint(min, max)
        nums.append(num)
    return nums

def suma_listas(l1:List[int], l2:List[int]) -> List[int]:
    suma= List[int] = []
    for i in range(len(l1)):
        suma=l1(i) + l2(i)
        suma.append(suma)
    return suma 

def main() -> None:
    MAX= 10
    lista1: List[int]= gen_rand(MAX, 1, 10)
    lista2: List[int]= gen_rand(MAX, 20, 40)
    lista3: List[int]= suma_listas(lista1, lista2)
    print(f"Lista 1: {lista1} - {len(lista1)}")
    print(f"Lista 2: {lista2} - {len(lista2)}")
    print(f"Lista 3: {lista3} - {len(lista3)}")

if __name__ == "__main__":
    main()