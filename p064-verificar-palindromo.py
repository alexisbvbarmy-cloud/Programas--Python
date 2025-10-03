## p064-verificar-palindromo.py
## Determinar si un número ingresado por el usuario es palíndromo. 

print("\033[2j\033[H")
print("Descubrir si el número es un palindromo")

num= int(input("Ingresa un número para determinar si es un palíndromo"))

ori=num
inv=0

if num<0:
    print("Los números negativos no son palíndromos")
else:
    while num>0:
        dig=num%10
        inv=inv*10+dig
        num=num//10

    if ori==inv:
        print("El número es palíndromo.")
    else:
        print("El número No es palíndromo")