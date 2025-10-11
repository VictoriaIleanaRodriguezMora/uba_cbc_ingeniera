"""
def sacaAcen(t): 
    con='áéíóú' 
    sin='aeiou' 
    # Arma el diccionario traductor transacción.
    traductor= str.maketrans(con, sin) 
    '''Aplica la traducción con el La informacion publica correcta para
    Mapeo de traductor á será ese envio no deberia haber sido mas
    cambiada por a, é por e''' 
    return t.translate(traductor)
#PPal
txt=input('Ingresá un texto: ')
txt=sacaAcen(txt.lower())
print('Texto sin acentos')
print(txt.capitalize())
"""


# LA INFORMACIÓN pública correcta para ese envío no debería haber sido más que una

# Facturación de Productos | cgo - codigo
# """
productos = {}

cgo = int(input('Ingrese código, 0 para terminar: '))
while cgo != 0:
    if cgo not in productos:
        desc = input('Descripción de %d: ' % cgo)
        unidad = input('Unidad de Medida de %s: ' % desc)
        precio = float(input('Precio unitario de %s: ' % desc))
        productos[cgo] = (desc, unidad, precio) 
        print(productos) # {11: ('v', 'unid', 32.5)}
        # 2da vez - {11: ('v', 'unid', 32.5), 25: ('a', 'gr', 0.65)}

    cgo = int(input('Ingrese código, 0 para terminar: '))

for cgo in productos:
    print()
    print(cgo, *productos[cgo]) # 11, velitas unid 32.5 
    print(cgo, productos[cgo]) # 11, (velitas, unid, 32.5)

# compras
total = 0
cgo = int(input('¿Qué lleva? 0 para salir: '))

# Si el código no existe, vuelve a pedirlo:
while cgo not in productos and cgo != 0:
    cgo = int(input('¿Qué lleva? 0 para salir: '))

# Si el código existe:
# %s 
while cgo != 0:
    # si cgo = 11 | productos[11] =  (velitas, unid, 32.5) | productos[11][0] = velitas
    cant = float(input('Cantidad de %s: ' % (productos[cgo][0]))) # (velitas, unid, 32.5)
    print("productos[cgo][0]", productos[cgo][0]) # velitas
    total += cant * productos[cgo][2] # 32.5
    print("total", total)
    cgo = int(input('¿Lleva algo más? 0 para salir: '))
    # Mientras el código ingresado no exista en el diccionario productos y no sea 0, sigue pidiéndolo, entra al bucle de la línea 52 finalizado este.
    while cgo not in productos and cgo != 0: # ¿Esta validación podría no estar ? mepa que no
        cgo = int(input('¿Qué lleva? 0 para salir: '))

# %.2f - formatea a 2 decimales
print('Debe abonar: $%.2f' % total, sep='')
# """



# Traducción de opciones de menú usando tuplas
"""
dificultad = ('', 'Alta', 'Media', 'Baja')
platos = []

nomPlato = input('Ingresá un plato, * para salir: ')
while nomPlato != '*':
    opc = 0
    while opc == 0:
        print('Dificultad:')
        for i in range(1, len(dificultad)):
            print('%d - %s' % (i, dificultad[i]))
        opc = int(input())
        if opc not in range(1, len(dificultad)):
            opc = 0

    platos.append([nomPlato, dificultad[opc]])
    nomPlato = input('Ingresá un plato, * para salir: ')

print('\nLista de Platos:')
for p in platos:
    print(*p)
"""

"""
dicci = {}
print('Datos de Clientes, * para terminar')

dni = input('DNI: ')
while dni != '*':
    nom = input('Nombre: ')
    ape = input('Apellido: ')
    edad = int(input('Edad: '))
    while edad not in range(18, 130):
        edad = int(input('Edad (entre 18 y 130): '))
    dicci[dni] = [nom, ape, edad]
    dni = input('DNI: ')

for pers in dicci:
    print(pers, dicci[pers][0], dicci[pers][1], dicci[pers][2])
"""


"""
dicci = {}
print('Datos de Clientes, * para terminar')

dni = input('DNI: ')
while dni != '*':
    nom = input('Nombre: ')
    ape = input('Apellido: ')
    edad = int(input('Edad: '))
    while edad not in range(18, 130):
        edad = int(input('Edad (entre 18 y 130): '))
    dicci[dni] = [nom, ape, edad]
    dni = input('DNI: ')

dicciOrden = sorted(dicci)

for pers in dicciOrden:
    print(pers, dicci[pers][0], dicci[pers][1], dicci[pers][2])
"""



