## p127-funcion-parametro.py
## Crear una función que reciba un parámetro

def saludar(nombre:str) -> None:
    
    print(f"Hola {nombre} bienvenido a Python, tu nombre tiene {len(nombre)} caracteres")
    print()

saludar("Otto Lidenbrock")
saludar("Henry Jekyll")
saludar("Juan Picaporte")