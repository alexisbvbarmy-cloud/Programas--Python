## p043-adivina-numero.py
## Simula un juego de azar donde el usuario adivina un número entre el 1 y el 50 

import random
print("\033[2j\033[H")
print("Bienvenido al juego de Adivina el Número")
print("Yo te soy un número entre el 1 y el 50 y tú tratas de adivinarlo")

num_sec= random.randint(1,50)
int_usu=0
cont_int=0

while True:
    int_usu=int(input("Tu número: "))
    cont_int+=1

    if int_usu<num_sec:
        print("Demasiado bajo, intenta algo más alto")
    elif int_usu>num_sec:
        print("Demasiado alto, intenta algo más bajo")
    else:
        print(f"\nFelicidades, Adivinaste el número secreto, es: {num_sec}")
        break

print("\nJuego Terminado")
