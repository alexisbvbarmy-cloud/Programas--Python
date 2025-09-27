## p041-sumar-consecutivos.py
## Suma números consecutivos 

print("\033[2j\033[H")
print("Rifa entre amigos para recaudar 100. Cuántos boletos necesito?")

c=0
suma=0

while c<=200:
    c+=1
    suma+=c
    print(f" {c}", end="")
    
    if suma >=100:
        print("\n\n¡Meta alcanzada!")
        print(f"Boletos= {c}")
        break

print("\nProceso Terminado..."+str(suma))