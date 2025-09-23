## p034-tipo-angulo.py
## Mostrar el tipo de ángulo 
## <90 agudo, ==90 recto, <180 obtuso, ==180 llano, <360 concavo, ==360 completo

print("\033[2j\033[H")
print("--- clasificador de Ángulos de acuerdo a su apmplitud")

angulo= int(input("Dame un ángulo en grados: "))

if angulo<0 or angulo>360:
    print(f"Tu águlo de {angulo} no está en el rango de 0 a 360, por lo tanto es invalido")
else:
    if angulo<90:
        print(f"El ángulo de {angulo} grados es un ángulo Agudo")    
    elif angulo==90:
        print(f"El ángulo de {angulo} grados es un ángulo Recto")    
    elif angulo<180:
        print(f"El ángulo de {angulo} grados es un ángulo Obtuso")    
    elif angulo==180:
        print(f"El ángulo de {angulo} grados es un ángulo Llano")    
    elif angulo<360:
        print(f"El ángulo de {angulo} grados es un ángulo Concavo")  
    else:
        print(f"El ángulo de {angulo} grados es un ángulo Completo")  
print("\nProceso Terminado")