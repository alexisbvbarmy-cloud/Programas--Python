# p020-numero-suerte.py
# Solicita al usuario su fecha de nacimiento 

print("-"*40)
print("Fecha de Nacimiento")
print("-"*40)

# Entrada

print("Ingresa tu año de nacimiento separando cada dígito con un espacio")
d1, d2, d3, d4= input().split()
d1, d2, d3, d4= int(d1), int(d2), int(d3), int(d4)

# Proceso
suma= d1+d2+d3+d4

# Salida
salida=(f"Los dígitos del año de nacimiento son: \n {d1, d2, d3, d4}\n"
f"La suma de los 4 dígitos de la fecha es: {d1} + {d2} + {d3} + {d4} = {suma}")
print(salida)
print("-"*40)