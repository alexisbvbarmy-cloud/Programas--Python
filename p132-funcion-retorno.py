## p132-funcion-retorno.py
## Simular sumar dos números y retornar la suma 
## función que regresa valores

def suma(n1:float, n2:float, n3:float) -> None:
    return n1 + n2 + n3

suma_resultado= suma(100, 30, 200, 300)
print(f"La suma es: {suma_resultado:.2f}")

print("Dame tres números separados por un ENTER")
a, b, c = float(input()), float(input()), float(input())
print(f"La suma de los números es: {suma(a,b,c):2f}")