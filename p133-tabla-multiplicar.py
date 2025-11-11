## p133-tabla-multiplicar.py
##

def tabla_multi(tabla:int, limit:int) -> None:
    print(f"Tabla de multiplicar del {tabla} hasta el {limit}")
    for i in range(1, limit+1):
        res= tabla * i
        print(f"{tabla} X {i} = {res}")
    print()

#tabla(5,10)

tabla= int(input("Ingresa la tabla de multiplicar que deseas: "))
limit= int(input("Ingresa el límite hasta donde deseas ultiplicar: "))

tabla_multi(tabla, limit)