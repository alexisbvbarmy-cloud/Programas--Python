## p040-multiplos-continue.py
## Imprime solo los múltiplos de 10 hasta el 200

print("\033[2j\033[H")
print("Buscando múltiplos de 10 entre 1 y 100")

c=0

while c<=200:
    c+=1
    if c%10!=0:
        continue # Ignora todo lo que sigue y salta a la siguiente iteración 
    # solo se ejecutea si el número es multiplo de 10 
    print(f" {c}", end="")

print("\nBúsqueda Terminada...")