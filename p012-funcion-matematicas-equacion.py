# p012-funcion-matematicas-equacion.py 
# Evaluar la función f(x,y) = 3x2 + sqrt 

import math as mt

x= 2
y= 2

# Evaluar la función utilizando la función pow
fxy1= 3*mt.pow(x,2) + mt.sqrt( (mt.pow(x,2) + mt.pow(y,2) + mt.pow(mt.e, mt.log(x)))) 

# Evaluando la función utilizando el operador de exponenciación (**)
fxy2= 3*x**2 + mt.sqrt( x**2 + y**2 + mt.exp(mt.log(x))) 

print(f"El resultado es : {fxy1:.4f}")
print(f"El resultado es : {fxy2:.4f}")