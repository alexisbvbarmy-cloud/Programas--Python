## p103-ciudades.py
## Leer nombres de ciudades en una lista, continuando hasta que el usuario introdusca el caracter $
## Imprimir cuántos elementos tiene la lista, lista ordenada en orden descentende, cuántas edades inician con una consonante y sus nombres.

print('\033[2J\033[H')
print("Nombres de ciudades")
print("Introduce nombres de ciudades (usa $ para terminar)")

ciudades= []

while True:
    ciudad = input("Ciudad: ").strip()
    if ciudad == '$':
        break
    if ciudad:
        ciudades.append(ciudad)

if not ciudades:
    print("\nNo se ingresaron ciudades")
else:
    print("\n" + "="*50)
    print("RESULTADOS:")
    print("="*50)
    print(f"• Total de ciudades: {len(ciudades)}")
    print(f"\n• Lista completa:")
    print("  ", ciudades)
    print(f"\n• Orden descendente:")
    print("  ", sorted(ciudades, reverse=True))


    consonantes = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    ciudades_consonante = [ciudad for ciudad in ciudades 
                          if ciudad and ciudad[0] in consonantes]
    
    print(f"\n• Ciudades que inician con consonante: {len(ciudades_consonante)}")
    if ciudades_consonante:
        print("  ", ciudades_consonante)
    else:
        print("  No hay ciudades con consonante inicial")