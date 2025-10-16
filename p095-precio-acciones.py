## p095-precio-acciones.py 
## Analisis de portafolio de acciones
## max - index

print('\033[2J\033[H')
print("Encontrar las acciones más alta y más baja en una semana.")

dias= ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']
precios= [150.25, 152.50, 149.75, 155.00, 153.20, 100.00]

precio_max = max(precios)
precio_min = min(precios)

p_max= precios.index(precio_max)
p_min= precios.index(precio_min)

print(f"Precios de las acciones en la semana: {precios}")
print(f"Días: {dias}")
print(f"EL precio más alto fue: {precio_max}. El día: {dias[p_max]}")
print(f"EL precio más bajo fue: {precio_min}. El día: {dias[p_min]}")