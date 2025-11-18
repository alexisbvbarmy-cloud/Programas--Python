## p144-mayor-menor.py
## Funciones para encontrar el mayor y el menor números de iuna lista

from typing import List

def mayor(lista:List[float]) -> float:
    num_may= lista[0]
    for numero in lista:
        if numero > num_may:
            num_may = numero
    return num_may

def menor(lista:List[float]) -> float:
    num_men= lista[0]
    for numero in lista:
        if numero < num_men:
            num_men = numero
    return num_men

def captura() -> List[float]:
    datos : List[float]=[]
    print("Ingresa un número ('fin' para terminar)")
    while True:
        entrada=input("Número: ")
        if entrada.lower()== 'fin': break
        try:
            numero= float(entrada)
            datos.append(numero)
        except ValueError:
            print("Debe ser un número")
    return datos


def main() -> None:
# numeros : List[float] = [20, 50, 80, 100, 10, 4, 25]

    numeros: List[float]= captura()

    if numeros:
        num_men= menor(numeros)
        num_may= mayor(numeros)

        print(f"Números ingresados: {numeros} - {len(numeros)}")
        print(f"El menor es: {num_men}")
        print(f"El mayor es: {num_may}")
    else:
        print("No se ingresaron núneros")

if __name__ == "__main__":
    main()