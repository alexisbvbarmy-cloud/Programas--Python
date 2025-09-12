# p010-operaciones-matematicas.py
# Demostrar el uso de los diferentes operadores aritmétricos con número 

print("="*60)
print("Calculadora de Operaciones Matemáticas")
print("="*60)

# Entrada
x= float(input("Valor de x ? "))
y= float(input("Valor de y ? "))

# Salida 
print(f"Suma           : {x:>6,.2f} + {y:<6,.2f}= {x + y:>10,.2f}")
print(f"Resta          : {x:>6,.2f} - {y:<6,.2f}= {x - y:>10,.2f}")
print(f"Multiplicación : {x:>6,.2f} * {y:<6,.2f}= {x * y:>10,.2f}")
print(f"División       : {x:>6,.2f} / {y:<6,.2f}= {x / y:>10,.2f}")
print(f"Módulo         : {x:>6,.2f} % {y:<6,.2f}= {x % y:>10,.2f}")
print(f"División Entera: {x:>6,.2f} // {y:<6,.2f}= {x // y:>10,.2f}")

print("="*60)

