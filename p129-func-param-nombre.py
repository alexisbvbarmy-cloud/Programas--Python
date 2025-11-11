## p129-func-param-nombre.py
## Función con 3 parámetros

def saludos(appaterno:str, apmaterno:str, nombre:str, edad:int) -> None:
    print(f"Hola {nombre} {appaterno} {apmaterno}, tienes {edad} años")

saludos("Cabral", "De Robles", "Alexis Federico", "27")
saludos(edad=27, nombre= "Alexis", appaterno= "Cabral", apmaterno= "De Robles", )
