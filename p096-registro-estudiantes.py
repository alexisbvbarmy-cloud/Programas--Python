## p096-registro-estudiantes.py
## Registro y analisis de asistentes a un evento

print('\033[2J\033[H')
print("Sistema de registro para eventos.")

print("Introduce los nombres y las edades de los asisstentes (* para terminar)")

nombres= []
edades= []

while True:
    nombre= input("Nombre del asistente: ")
    if nombre== '*': break
    try:
        edad= int(input("Edad: "))
        nombres.append(nombre)
        edades.append(edad)
    except ValueError: 
        print("Valos erroneo.")

if not nombres:
    print("No hay datos para procesar")
else:
    print("Asistentes mayores de edad:")
    encontrados: False
    for i in range(len(nombres)):
        if edades(i)>=18:
            print(f"Nombre: {nombres[i]}, Edad: {edades[i]}")
            encontrados= True
        if not encontrados:
            print("No hay mayores de edad.")

edad_max= max(edades)
p_max= edades.index(edad_max)
nombre_max= nombres[p_max]

print("\nEl reconocimiento a la persona de mayor edad es para: ")
print(f"Nombre: {nombre_max} con edad de {edad_max} años.")