## p027-calcular-paga-extra.py
## Calcular la paga extra de un trabajador

print("\033[2j\033[H")
print("\033[31mCalcular la paga extra de un trabajador\033[0m")

print("Introduce los datos del trabajador")
nombre=input("Nombre:")
horas= int(input("Horas trabajadas:"))
paga_hora= float(input("Paga por hora:"))


# Proceso 
horas_normales = 30
horas_extra= 0
paga_normal= 0
paga_extra= 0
total= 0

if horas <= horas_normales:
    paga_normal= horas*paga_hora
    total = paga_normal
else: 
    paga_normal= horas_normales*paga_hora
    horas_extra=horas-horas_normales
    paga_extra=horas_extra*(paga_hora*2)
    total=paga_normal+paga_extra

print("\nCalculo completo")
print(f"{nombre} trabajo {horas} horas, a una paga de {paga_hora} pesos por hora, horas extra: {horas_extra}")
print(f"Paga normal: ${paga_normal:13,.2f}")
print(f"Paga extra: ${paga_extra:13,.2f}")
print(f"Total: ${total:13,.2f}")
