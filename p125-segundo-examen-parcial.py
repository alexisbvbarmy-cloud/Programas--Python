## p125-segundo-examen-parcial.py
## Inventario de productos de de una tienda de electrónicos
## Capturar: 
# Nombre del producto
# precio (valor numérico)
# categoria (ej. 'Laptops', 'Celulares', 'Audio')
# proveedor (el nombre del distribuidor, ej. 'Sony', 'HP', 'Generico')
# stock (cantidad en inventario, ej. 25)
## Al ingresar un nombre del producto vacío, Procesar e Imprimir:
# Total de productos registrados. 4
# Cuántos productos por categoría.
# Cuántos productos por proveedor.
# La suma total del stock y el promedio de stock por producto.
# La suma total de precios (considerando un solo precio por producto) y el precio promedio.
# El nombre y precio del producto más caro y del más barato.

print('\033[H\033[J')
print('Inventario de productos electrónicos\n')
print('-'*60)

inv=[]
cant=1

# Solicita al usuario los datos del producto
while True:
    print("Producto #" +str(cant))
    nombre= input("nombre del producto: ").strip()

    if nombre== '':
        break
    
    precio= float(input("Precio: "))
    cat= input("Categoría (Laptop/Celular/Audio/Otros): ").strip()
    prov= input("Proveedor: ").strip()
    stock= int(input("Stock: "))

    prod={
        'nombre': nombre,
        'precio': precio,
        'categoria': cat,
        'proveedor': prov,
        'stock': stock  
    }

    inv.append(prod)
    cant+=1

## Proceso y reporte de inventario
if len(inv) ==0:
    print("No se ingresaron productos.")
else:
    print("\n" + "="*60)
    print("REPORTES DE INVENTARIO")
    print("="*60)  

# Imprime Datos Crudos 
    print("\n1. DATOS CRUDOS:")
    print(inv)

# Tabla
    print("\n2. FORMATO TABULAR:")
    print("-" * 80)
    print("Nombre           Precio     Categoría    Proveedor      Stock")
    print("-" * 80)
    
    for prod in inv:
        nombre = prod['nombre'][:15]
        precio = prod['precio']
        categoria = prod['categoria'][:10]
        proveedor = prod['proveedor'][:12]
        stock = prod['stock']
        print(f"{nombre:15} ${precio:8.2f} {categoria:12} {proveedor:14} {stock:8}")
    print("-" * 80)

## Resúmen del inventario
    print("\n3. RESUMEN DEL INVENTARIO:")
    print("-" * 40)
    tot_prod = len(inv)
    print("Total de productos registrados: " + str(tot_prod))

# Productos por categoría 
    cats = {}
    for prod in inv:
        cat = prod['categoria']
        if cat in cats:
            cats[cat] += 1
        else:
            cats[cat] = 1
    print("\nProductos por categoría:")
    for cat in cats:
        print("  " + cat + ": " + str(cats[cat]) + " producto(s)")

# Productos por provedor 
    proveedores = {}
    for producto in inv:
        prov = producto['proveedor']
        if prov in proveedores:
            proveedores[prov] += 1
        else:
                proveedores[prov] = 1
        
    print("\nProductos por proveedor:")
    for prov in proveedores:
        print("  " + prov + ": " + str(proveedores[prov]) + " producto(s)")

# Estadísticas del stock
    total_stock = 0
    for producto in inv:
        total_stock += producto['stock']
    promedio_stock = total_stock / tot_prod
    
    print("\nEstadísticas de stock:")
    print("  Suma total del stock: " + str(total_stock))
    print("  Promedio de stock por producto: " + str(round(promedio_stock, 1)))
    
# Estadísticas de precios
    suma_precios = 0
    for producto in inv:
        suma_precios += producto['precio']
    promedio_precio = suma_precios / tot_prod

# Producto más caro y más barato
    producto_caro = inv[0]
    producto_barato = inv[0]
    
    for producto in inv:
        if producto['precio'] > producto_caro['precio']:
            producto_caro = producto
        if producto['precio'] < producto_barato['precio']:
            producto_barato = producto

    print("\nEstadísticas de precios:")
    print("  Suma total de precios: $" + str(round(suma_precios, 2)))
    print("  Precio promedio: $" + str(round(promedio_precio, 2)))
    print("  Producto más caro: " + producto_caro['nombre'] + " - $" + str(round(producto_caro['precio'], 2)))
    print("  Producto más barato: " + producto_barato['nombre'] + " - $" + str(round(producto_barato['precio'], 2)))