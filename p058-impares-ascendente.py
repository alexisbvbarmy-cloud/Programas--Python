## p058-impares-ascendente.p
## Imprimir los números impares en un rango ascendente desde 1 hasta un número que el usuario elija

print("\033[2j\033[H")
print("Imprime números impares")

inicio=1
fin= int(input("Hasta qué número lo quieres?:"))

numero=inicio
suma=0

while numero<=fin:
    if numero%2!=0:
        print(f"{numero}")
        suma+=numero
    numero+=1
    
print("\nSecuencia Completada")
print(f"La suma de los números impares es: {suma}")