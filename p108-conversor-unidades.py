## p108-conversor-unidades.py
## Conversor de unidades de longitud usando diccionarios

conv= {
    'km':1000,
    'm':1,
    'cm':0.1,
    'mm':0.001
}

print('\033[H\033[J')
print('Conversor de unidades de longitud usando diccionarios\n')

while True:
    try:
        long= int(input("Dame la longitud en metros: "))
    except ValueError:
        continue


    while True:
        uni= input("A qué unidad deseas convertir: (km, m, cm, mm): ")
        if uni in conv: break
        else: continue

    res= long/conv[uni]

    print(f"{long:,.4f} {uni} son {res:,.4f} metros")