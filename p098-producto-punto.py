## p098-producto-punto.py
## Calcula el producto punto de dos vectores

print('\033[2J\033[H')
print("Calcula el producto punto de dos vectores.")

A= [1, 2, -5]
B= [4, -2, -1]
C= []

print(f"Vector A: {A}")
print(f"Vector B: {B}")

if len(A)==len(B):
    print("Calculando el producto punto:")
    for i in range(len(A)):
        prod=A[i]*B[i]
        C.append(prod)
    print(f"EL vector C: {C}")
    print(f"El producto punto es: {sum(C)}")
else: 
    print("Los vectores deben ser del mismo tamaño")