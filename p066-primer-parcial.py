## p066-primer-parcial.py
## Administración de las ventas del cine Python

## Objetivo: Crear un programa que administre la venta de boletos en el cine
## Nombre del Alumno: Alexis Federico Cabral de Robles
## Matrícula: 111808
## Materia: Computación Aplicada
## Examen: Primer Parcial

# --- Inicialización de Contadores y Acumuladores ---
# Aquí se declaran todas las variables que necesitarás para guardar los datos

# --- Contadores de Asistentes ---
precio_boleto=0
total_estudiantes = total_adultos= total_tercera_edad= total_acad= total_hombres= total_mujeres= 0
total_asistentes = 0
total_rechazados = 0
suma_edades = 0

# --- Acumuladores de Ingresos ---
ingresos_estudiantes = 0.0
ingresos_adultos=0
ingresos_tercera_edad=0
ingresos_acad=0
ingresos_hombres=0
ingresos_mujeres=0
ingresos_totales = 0.0

# --- Precios de los Boletos (constantes) ---
PRECIO_ESTUDIANTE = 50.0
PRECIO_ADULTO = 90.0
PRECIO_TERCERA_EDAD = 60.0
PRECIO_ACAD = 70.0


print('\033[2J\033[H')
print("--- Sistema de Venta de Boletos de Cine ---")

# --- Ciclo Principal para la Venta de Boletos ---
# Usaremos un ciclo while para registrar ventas hasta que el usuario decida parar.
continuar_venta = "s"
while continuar_venta == "s":

    print("\n--- Nueva Venta ---")
    # --- 1. Solicitud de Datos ---
    edad = int(input("Introduce la edad del comprador: "))
    
    # --- 2. Validación de Edad (Clasificación B) ---
    # La película es para mayores de 13 años.
    
    if edad > 13:
        tipo= input("Indica el tipo de comprador: (E)studiante, (A)dulto, (T)ercera edad, (Ac)adémico").upper()
        sexo= input("Indica el género del comprador: (H)ombre, (M)ujer").upper()
        # Si la edad es permitida, procede con la venta.
        # Muestra el mensaje de bienvenida con los datos registrados
        print(f"¡Bienvenido(a)!... tienes {edad} años, eres un {tipo}, y tu sexo es: {sexo}")
        
        # --- 3. Actualización de Estadísticas Generales ---
        if tipo=='E':
            total_estudiantes +=1
            precio_boleto=PRECIO_ESTUDIANTE
            ingresos_estudiantes +=precio_boleto
        elif tipo=='A':
            total_adultos+=1
            precio_boleto=PRECIO_ADULTO
            ingresos_adultos +=precio_boleto
        elif tipo=='T':
            total_tercera_edad +=1
            precio_boleto=PRECIO_TERCERA_EDAD
            ingresos_tercera_edad +=precio_boleto
        elif tipo=='AC':
            total_acad+=1
            precio_boleto=PRECIO_ACAD
            ingresos_acad +=precio_boleto
        

        # --- 4. Cálculo de Costo y Actualización de Contadores Específicos ---
        if sexo=='H':
            precio_boleto==PRECIO_ADULTO
            total_hombres+=1
            ingresos_hombres+=precio_boleto
        if sexo=='M':
            precio_boleto==PRECIO_ADULTO
            total_mujeres+=1
            ingresos_mujeres+=precio_boleto

        total_asistentes+=1
        ingresos_totales+=precio_boleto
        suma_edades+=edad
     
    else:
        # Si la edad no es permitida, muestra un mensaje y actualiza el contador ()
        print("ACCESO DENEGADO: El comprador es menor de 13 años.")
        total_rechazados+=1
        
    # Pregunta al usuario si desea registrar otra venta.
    continuar_venta = input("\n¿Deseas registrar otra venta? (S/N): ").lower()

# --- FIN DEL CICLO ---

# --- 5. Cálculo de Promedio ---
# Calcula el promedio de edad. Cuidado con la división entre cero si no hubo asistentes.
promedio_edad = 0
if total_asistentes > 0:
     promedio_edad = suma_edades/total_asistentes


# --- 6. Impresión del Reporte Final ---
print("\n*** REPORTE FINAL DE LA FUNCIÓN ***")

print("\n--- Estadísticas del Público ---")
print(f"Total de Asistentes: {total_asistentes}")
print(f"Total de Rechazados por la edad: {total_rechazados}")
print(f"Total de Estudiantes: {total_estudiantes}")
print(f"Total de Adultos: {total_adultos}")
print(f"Total de la Tercera Edad: {total_tercera_edad}")
print(f"Total de Académicos: {total_acad}")
print(f"Total de Hombres: {total_hombres}")
print(f"Total de Mujeres: {total_mujeres}")
print(f"El promedio de las edades es: {promedio_edad}")
# Imprime todos los totales de asistentes por tipo y sexo.
 
print("\n--- Reporte de Ingresos ---")
print(f"Ingresos de Estudiantes: ${ingresos_estudiantes:.4f}")
print(f"Ingresos de Adultos: ${ingresos_adultos:.4f}")
print(f"Ingresos de Tercera Edad: ${ingresos_tercera_edad:.4f}")
print(f"Ingresos de Académicos: ${ingresos_acad:.4f}")
print(f"Ingresos de Hombres: ${ingresos_hombres:.4f}")
print(f"Ingresos de Mujeres: ${ingresos_mujeres:.4f}")
print(f"Ingreso Total de la Función: ${ingresos_totales:.4f}")
# Imprime todos los ingresos por tipo de comprador y el total general.
# Utiliza formato para mostrar dos decimales en el dinero.

print("\n--- Rentabilidad ---")
# --- 7. Mensaje de Rentabilidad ---
if ingresos_totales<1500:
    print(">>>La función generó BAJAS ganancias")
elif ingresos_totales>=1500 and ingresos_totales<=3500:
    print(">>>La función generó ganancias MODERADAS")
elif ingresos_totales>3500:
    print(">>>La función generó BUENAS ganancias")


# Usa una estructura if/elif/else para determinar si las ganancias
# fueron BAJAS, MODERADAS o BUENAS, basándote en los ingresos totales.


"""
Preguntas: Explica con tus palabras

1. Imagina que el cine decide implementar una promoción: los martes, todos los boletos de Adulto tendrán un 20% de descuento. 
¿Qué cambios tendrías que hacer en tu código para agregar esta funcionalidad? 
Menciona qué nueva pregunta le harías al usuario y en qué parte del código agregarías la nueva lógica.

## Después de pedir la edad del usuario se agrega la pregunta "Qué día es hoy?". Después se agrega un nuevo ciclo if/else en el que según qué día de las semana es se aplica el descuento:
El nuevo ciclo se agrega después de la linea 46 para que el programa aplique o no el descuento antes de determinar el tipo de comprador.

2. Supongamos que, al probar tu programa, el "Total Recaudado en General" siempre te da un resultado incorrecto, 
aunque los ingresos por cada tipo de comprador parecen correctos. 
Describe, paso a paso, qué harías para encontrar el error. 
¿En qué líneas específicas de tu código pondrías atención para verificar los valores y solucionar el problema?

## Buscar las líneas de código en donde asingnamos la operación del total recaudado (en éste caso líneas 87-89) y verificar si la lógica de la suma es correcta o si está sumando las variables correctas.
Ejemplo: 
ingresos_estudiantes += precio_boleto  
ingresos_totales += ingresos_estudiantes

En éste caso la suma da resultado incorrecto porque esa lógica de operación suma el acumulado cada vez, duplicando el monto. 
"""