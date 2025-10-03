## p059-pares-descendente.py
## Imprime los número pares y su suma en un rango descendente desde 100 hasta un número que elija el usuario

print("\033[2j\033[H")
print("Imprime números pares en orden descendente desde 100")

inicio=100
fin= int(input("Hasta qué número lo quieres?:"))

numero=inicio
suma=0

while numero>=fin:
    if numero%2==0:
        print(f"{numero}")
        suma+=numero
    numero-=1
    
print("\nSecuencia Completada")
print(f"La suma de los números pares es: {suma}")