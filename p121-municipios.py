## p121-municipios.py
## Gestión de un padrón municipal, usando conjuntos

municipios = {'Zacatecas', 'Guadalupe', 'Jerez', 'Fresnillo', 'Fresnillo'}

print('\033[H\033[J')
print("Gestión de un padrón municipal, usando conjuntos")

print(f"Los municipios: {municipios} - {len(municipios)} - {type(municipios)}")

print("\nTodos los municipios uno a uno")
for municipio in municipios:
    print(municipio, end=' | ')

print("\nAlta de un municipio al padrón: Teul")
municipios.add("Teul")
print(f"Los municipios: {municipios} - {len(municipios)} - {type(municipios)}")

print("\nAgregar varios municipios: Luis Moya, Ojocaliente, Tepetongo")
municipios.update({'Luis Moya', 'Ojocaliente', 'Tepetongo'})
print(f"Los municipios: {municipios} - {len(municipios)} - {type(municipios)}")

print("\nBaja de un municipio con remove")
municipios.remove("Zacatecas")
print(f"Los municipios: {municipios} - {len(municipios)} - {type(municipios)}")

print("\nBaja de un municipio con discard. Ojocaliente")
municipios.discard("Ojocaliente")
print(f"Los municipios: {municipios} - {len(municipios)} - {type(municipios)}")

print("\nBaja del padrón con pop()")
eliminado= municipios.pop()
print(f"Los municipios: {municipios} - {len(municipios)} - {type(municipios)} - {eliminado}")

print("\nLimpiar el padrón con .clear() ")
municipios.clear()
print(f"Los municipios: {municipios} - {len(municipios)} - {type(municipios)}")