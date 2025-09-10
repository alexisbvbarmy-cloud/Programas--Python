# p008-entrada-con-espacios.py
# Leer tres números enteros separados por un espacio 

print("Entrada de varios valores separados por un espacio")

print("Dame tres números, separados po un espacio")

n1, n2, n3= input().split() # leo una línea y lo separo en base el espacio (split)

n1, n2, n3= int(n1), int(n2), int(n3)

print("Los valores introducidos son:")
print(n1, n2, n3)