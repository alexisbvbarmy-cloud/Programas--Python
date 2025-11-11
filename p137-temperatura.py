## p137-temperatura.py
## Más de una función 

def cent_farh(c:float) -> float:
    return (c*9/5)+32

def farh_cent(f:float) -> float:
    return(f-32)*5/9

def main() -> None:
    print("Conversión de Temperaturas")
    print("Centígrados -> Fahrenheit")
    print("Fahrenheit -> Centigrados")
    op=int(input("Elige: "))
    if op==1:
        print("Dame los grados centrígrados: ")
        c= float(input())
        f= cent_farh(c)
        print(f"{c} centígrados son {f} Fahrenheit")
    elif op==1:
        print("Dame los grados fahrenheit: ")
        f= float(input())
        c= farh_cent(f)
        print(f"{c} Fahrenheit son {f} centígrados")
    else: 
        print("Opción inválida")

if __name__=="__main__":
    main()
