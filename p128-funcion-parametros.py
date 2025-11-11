## p128-funcion-parametros.py
## Función con múltiples parámetros, se debe llamar con el mismo npumero de parámetros y en el mismo orden.

def salu2(apaterno:str, nombre:str) -> None:
    print(f"Hola {nombre}, {apaterno}")
    print()

salu2("Pérez", "Juan")
#salu2("castaneda")
#salu2("Castanmeda", "Ramírez", "Carlos")