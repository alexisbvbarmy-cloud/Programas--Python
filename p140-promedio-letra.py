## p140-promedio-letra.py
##

def cal_letra(prom: float) -> tuple[str, str]:
    let=""
    men=""
    if 90 <= prom <= 100:
        let="A"; men="Escelente"
    elif 80 <= prom <= 100:
        let="B"; men="Bien"
    elif 70 <= prom <= 100:
        let="C"; men="Suficiente"
    elif 60 <= prom <= 100:
        let="D"; men="Deficiente"
    elif 0 <= prom <= 60:
        let="F"; men="Reprobado"
    else:
        let=""; men="Calificación inválida"

    return let, men

#l,m=cal_letra(70)
#print(f"Para un promedio de 70: corresponde: {l} - {m}")

def main() -> None:
    prom=float(input("Dame el promedio: "))
    letra, mensaje= cal_letra(prom)
    if letra:
        print(f"Calificación {letra} - {mensaje}")
    else: 
        print(mensaje)

if __name__== "__main__":
    main() 