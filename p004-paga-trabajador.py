# p004-paga-trabajador.py
# Calcula la paga de un trabajador  

print("Calculando la paga de un trabajador")

# Entrada
print("Nombre: ")
nombre= input()
print("Horas Trabajadas: ")
horas= int(input())
print("Paga por hora: ")
paga= float(input())

#Proceso
tasa= 0.09 # impuesto de hacienda 
pagabruta= horas*paga
impuesto= pagabruta*tasa
paganeta= pagabruta-impuesto 

#Salida 
print("\nResumen de pagos: \n")
print(f"El trabajdor {nombre}, trabajó {horas} diarias, con una paga de {paga} pesos por hora, impuesto de {tasa}%")
print(f"Paga bruta  : {pagabruta:.2f}")
print(f"Impuesto    : {impuesto:.2f}")
print(f"Paga neta   : {paganeta:.2f}")