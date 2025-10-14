## p088-modificar-lista.py
## Muestra cómo modificar los elementos de una lista

print('\033[2J\033[H')
print("Modificar los elementos de una lista")

califs=[10,9.8,5,6.5,9.8,7,7,6.2,9,5]

print(f"Todasl las calificaciones: {califs} - {len(califs)}")

print("\nModificar [0] y [1] como 7 y 7:")
califs[0]=7
califs[1]=7
print(f"Resulado: {califs} - {len(califs)}")

print("\nModificar el rango [2:5] (5 no se inclute) con 9, 9 y 9:")
califs[2:5]==9
print(f"Resultado: {califs} - {len(califs)}")