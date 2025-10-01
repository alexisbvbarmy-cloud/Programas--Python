## p056-contador-vocales.py
## Contador de cvocales y consonantes 

while True:
    print("\033[2j\033[H")
    print("contador de consonante y vocales")
    frase= input("Introduce una frase: ")

    vocales= consonantes = otros = 0
    indice=0

    while indice<len(frase):
        caracter=frase[indice] # tomamos el caracter correspondiente de la frase

        if caracter>='a' and caracter<='z': # verificamos que sea una letra 
            print(caracter)
            if caracter in 'aeiou': # es vocal
                vocales+=1
            else:
                consonantes+=1 # es consonante
        else:
            otros+=1 # es otro


        indice+=1 # paso al siguiente caracter
    
    print("Analisis de la frase")
    print(f"Número de vocales: {vocales}")
    print(f"Número de consonantes: {consonantes}")
    print(f"Número de otros: {otros}")

    if input("\nDeseas continuar? [S/N]").upper()=='N': break

print("\nProceso Terminado")