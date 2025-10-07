## p075-cifrado-cesar.py
## Cifra un menasje usando el cifrado de Cesar

while True:
    print('\033[2J\033[H')
    print("Cifrado de un mensaje usando el cifrado de Cesar")
    mensaje_original= input("Ingresa el mensaje a cifrar")
    desplazamiento= int(input("Desplazamiento (número): "))
    mensaje_cifrado=""

    for caracter in mensaje_original:
        if caracter.isalpha():
            codigo_ascii= ord(caracter)
            print(codigo_ascii)
            base= ord("a") if caracter.islower() else ord("A")
            codigo_nuevo= base + (codigo_ascii-base+desplazamiento)%26
            mensaje_cifrado+= chr(codigo_nuevo)
        else:
            mensaje_cifrado+=caracter
        
    print(f"Mensaje original: {mensaje_original}")
    print(f"Mensaje Cifrado: {mensaje_cifrado}")

    if input("\n\nDeseas continuar (S/N)").upper()=="N": break

print("Proceso Terminado")