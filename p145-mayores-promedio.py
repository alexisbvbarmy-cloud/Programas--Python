## p145-mayores-promedio.py

from typing import List

def prom_list(lista:List[float]) -> float:
    suma=0
    if not lista:
        return 0.0
    for numero in lista:
        suma+=numero
    return suma/len(lista)

def mayores_prom(lista:List[float], prom:float) -> List[float]:
    mayores: List[float] =[]
    for numero in lista:
        if numero > prom:
            mayores.append(numero)
    return mayores

def main() -> None:
    numeros: List[float] = [1.5, 2.3, 3.7, 4.0, 5.5]
    prom= prom_list
    resulado= mayores_prom(numeros, prom)
    print(f"Números mayores al promedio: {resulado} - {len(resulado)}")
    print(f"El promedio es: {prom}")

if __name__ == "__main__":
    main()