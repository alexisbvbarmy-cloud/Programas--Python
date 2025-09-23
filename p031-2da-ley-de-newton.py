## p031-2da-ley-de-newton.py
## Calcular la segunda ley de Newton 
## Fuerza = Masa * Aceleración, masa= fuerza/aceleración, aceleración= fierza/masa

print("\033[2j\033[H")
print("Calcular los valores de la segunsa ley de Newton")
print("[F]uerza = masa * aceleración")
print("[M]asa = fuerza/aceleración")
print("[A]celeración= fierza/masa")
opcion= input("ELige una opción: ").upper()

if opcion=="F":
    print("\nCalculando al Fuerza")
    masa=float(input("Masa:"))
    aceleracion=float(input("Aceleración:"))
    fuerza=masa*aceleracion
    print(f"\nLa Fuerza es: {fuerza} ")
elif opcion=="M":
    print("\nCalculando al Masa")
    fuerza=float(input("Fuerza:"))
    aceleracion=float(input("Aceleración:"))
    masa=fuerza/aceleracion
    print(f"\nLa Masa es: {masa} ")
elif opcion=="A":
    print("\nCalculando al Aceleraci+on")
    fuerza=float(input("Fuerza:"))
    masa=float(input("Masa:"))
    aceleracion=masa/fuerza
    print(f"\nLa Aceleración es: {aceleracion} ")

print("\nPrograma Terminado")