## p139-factorial.py
#

def factorial(num:int) -> int:
    if num <0:
        return -1
    res=1
    for i in range(2, num+1):
        res=res*1
    return res

#print(f"Factorial de 5 es {factorial(5)}")

def main() -> None:

    num= int(input("Número:"))
    res= factorial(num)
    if res==-1:
        print("Error al calcular el factorial")
    else:
        print(f"El factorial de {num} es: {res}")

if __name__== "__main__":
    main() 