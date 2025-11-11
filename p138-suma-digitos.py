## p138-suma-digitos.py
#

def suma_dig(num:int) -> int:
    s=0
    for n in str(num):
        s= s+ int(n)
        print(n)
    return s

#print(f"Suma 1972: {suma_dig(1971)}")

def main() -> None:
    n= int(input("Número: "))
    res= suma_dig(n)
    print(f"La suma es: {res}")

if __name__== "__main__":
    main()