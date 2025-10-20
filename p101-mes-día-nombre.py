## p101-mes-día-nombre.py
## Leer un número del mes. 4). Guardar los días de cada mes en una lista y los nombres de los meses en otra
## lista. Asumir 28 días para febrero. Imprimir el nombre del mes y la cantidad de días del mes correspondiente (ej.
## marzo, 30).

print('\033[2J\033[H')
print("----- Procesador de fechas -----")

meses= ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(12):
    print(f"{i+1}. {meses[i]}: {dias[i]} días")

print("\n" + "="*40)

while True:
    try:
        num = int(input("\nIntroduce el número del mes (1-12), 0 para terminar: "))
        
        if num == 0:
            print("¡Programa terminado!")
            break
            
        if 1 <= num <= 12:
            indice = num - 1
            print(f"✓ Mes: {meses[indice]}")
            print(f"✓ Días: {dias[indice]}")
            print(f"✓ Información: El mes de {meses[indice]} tiene {dias[indice]} días")
        else:
            print("❌ Error: El número debe estar entre 1 y 12")
            
    except ValueError:
        print("❌ Error: Por favor ingresa un número válido (1-12)")