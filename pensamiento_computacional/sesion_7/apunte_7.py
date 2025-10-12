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
"""
productos = {}

cgo = int(input('Ingrese código, 0 para terminar: '))
while cgo != 0:
    if cgo not in productos:
        desc = input('Descripción de %d: ' % cgo)
        print('desc ', desc) # velitas
        unidad = input('Unidad de Medida de %s: ' % desc)
        print('unidad ', unidad) # unid
        precio = float(input('Precio unitario de %s: ' % desc))
        print('precio ', precio) # 32.5
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
    while cgo not in productos and cgo != 0: # ESTE WHILE ¿Esta validación podría no estar ? mepa que no
        cgo = int(input('¿Qué más lleva? 0 para salir: '))

# %.2f - formatea a 2 decimales
print('Debe abonar: $%.2f' % total, sep='')
print('Debe abonar: $%.2f' % total)
"""



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
        opc = int(input()) # 1, 2, 3
        # si ingreso 5, me vuelve al while
        if opc not in range(1, len(dificultad)):
            opc = 0

    platos.append([nomPlato, dificultad[opc]])
    nomPlato = input('Ingresá un plato, * para salir: ')

print('\nLista de Platos:')
for p in platos:
    print(*p)
"""

# """
# traducción de opciones de menú usando diccionarios
"""
dificultad = {1: 'Alta', 2: 'Media', 3: 'Baja'}
platos = []

nomPlato = input('Ingresá un plato, * para salir: ')
while nomPlato != '*':
    opc = 0
    while opc == 0:
        print('Dificultad:')
        for i in dificultad:
            print('%d -' % i, dificultad[i])
        opc = int(input('Elegí una opción: '))
        if opc not in dificultad:
            opc = 0

    platos.append([nomPlato, dificultad[opc]])
    nomPlato = input('Ingresá un plato, * para salir: ')

print('\nLista de Platos:')
for p in platos:
    print(*p)

"""

# Datos de Clientes
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

# Pero ¿Y si en realidad queremos ver toda la información, pero ordenada por el valor de la clave?
# """
dicci = {}
print('Datos de Clientes, * para terminar')

dni = input('DNI: ') 
while dni != '*': # pide dni cuando ya tiene todos los otros datos, seria cuando cargas una nueva persona 
    nom = input('Nombre: ')
    ape = input('Apellido: ')
    edad = int(input('Edad: '))
    while edad not in range(18, 130):
        edad = int(input('Edad (entre 18 y 130): '))
    dicci[dni] = [nom, ape, edad]
    print("dicci ",dicci) # {'18023569': ['A', 'G', 56], '17895822': ['M', 'S', 66]}
    dni = input('DNI: ')

# aplicando la función sorted a un diccionario devuelve una lista con las claves ordenadas. SOLO CON LAS CLAVES, no su contenido ordenado
dicciOrden = sorted(dicci) #  ['17895822', '18023569']
print("dicciOrden ",dicciOrden)

for pers in dicciOrden:
    # pers es el DNI, pq son las claves de dicci
    print(pers, dicci[pers][0], dicci[pers][1], dicci[pers][2])
# """



