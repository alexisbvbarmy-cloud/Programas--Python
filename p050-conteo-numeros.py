## p042-conteo-numeros.py
## Permite ingresar n números, se detiene al intriducir 999 y muestra estadísticas 

print("\033[2j\033[H")
print("Estadísticas con números que el usuario proporciona")

cuenta= 0
suma=0
cp= cn=c2=0

while True:
    num=int(input("Introduce un número entero:"))
    if num==999:
        print("Detectando sentinela 999, me voy!")
        break
    cuenta+=1
    suma+=num
    if num>0: 
        cp+=1
    elif num<0:
        cn+=1
    else:
        c2+=1

print("\n Resumen Final ")
print(f"Números introducidos: {cuenta}")
print(f"La suma es: {suma}")
print(f"Positivos: {cp}")
print(f"Negativos: {cn}")
print(f"Ceros: {c2}")