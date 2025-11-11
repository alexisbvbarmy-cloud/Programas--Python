## p130-func-param-defecto.py
## Calcular IVA

def calc_tot(monto:float, iva:float=0.16) -> float:
    return monto + (monto+iva)

res= calc_tot(1000)
print(f"Total 1: $ {res:,.2f}")

print(f"total 2: $ {calc_tot(1000,0.08):,.2f}")
