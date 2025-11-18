## p148-nombres.py
## Función que tome dos lista de cadenas y las procese 

from typing import List

def une_proc(l1:List[str], l2:List[str]) -> List[str]:
    todo= l1 + l2
    inv=todo[::-1]
    mayus=List[str]=[]
    for nombre in inv:
        mayus.append(nombre.upper())
    return mayus

def entrada() -> List[str]:
    datos: List[str]=[]
    print("Introduce Nombres (Vacío para terminar)")
    while True:
        nombre= input("Nombre: ")
        if nombre== "": break
    return datos

nombres1: List[str] = ["Ana", "Luis", "Carlos", "Martha", "Sofía"]
nombres2: List[str] = entrada()
todo= List[str]= une_proc(nombres1, nombres2)

print(f"Lista nombres 1: {nombres1} - {len(nombres1)}")
print(f"Lista nombres 2: {nombres2} - {len(nombres2)}")
print(f"Todo : {todo} - {len(todo)}")
