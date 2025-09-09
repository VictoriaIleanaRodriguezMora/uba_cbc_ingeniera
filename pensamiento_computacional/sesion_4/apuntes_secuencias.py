#arma menú de opciones y devuelve selección entera recibe tupla con opciones de menú'''
'''
def menu(opciones):
    print('Selecciona una opción')
    for i in range(1, len(opciones)):
        print(i, '-', opciones[i])
    opc = int(input())
    while opc not in range(1, len(opciones)):
        opc=int(input())
    return opc

quesos = ('', 'cheddar', 'dambo', 'muzzarela', 'brie', 'cremoso', 'sin queso')
panes = ('', 'semillas', 'árabe', 'centeno', 'pebete', 'francés')
carnes = ('', 'hamburguesa', 'jamón cocido', 'jamón crudo', 'lomito', 'salchicha', 'mortadela', 'veggie')
salsas = ('', 'mayonesa', 'guacamole', 'ketchup', 'salsa golf', 'barbacoa', 
'ranch', 'sin salsa')
acomp = ('', 'tomate', 'lechuga', 'pepinillos', 'verduras cocidas', 
'berenjena escabeche', 'sin extras')
print('Armá tu sandwich')

op1=menu(panes)
op2=menu(carnes)
op3=menu(quesos)
op4=menu(acomp)
op5=menu(salsas)
print('Tu pedido de sandwich de pan', panes[op1], 'saldrá pronto')
print('Detalle:', carnes[op2], quesos[op3], acomp[op4], salsas[op5], sep='\n')
'''
'''

a=(1,2)
a=a*3
print(a) # (1, 2, 1, 2, 1, 2)
'''

s = [10, 20, 30, 20, 40]

# [s.index(busco, inicio, fin)]
# FIN no se incluye
'''
print(s.index(20))        # 1 (la primera vez que aparece 20)
print(s.index(20, 2))     # 3 (busca desde el índice 2 en adelante)
print(s.index(20, 2, 4))  # 3 (busca desde 2 hasta antes de 4)
'''


# Ej de carga e impresión de listas
'''
nombres = []
nom = input('Ingrese un nombre, * para salir:')
while nom!= '*':
    nombres.append(nom)
    nom = input('Ingrese un nombre, * para salir:')

print('Lista de Nombres')
print(nombres)
print('Salida detallada')

for n in nombres:
    print("--->",n)
'''


# Ejemplo con Listas
# En este caso creamos una lista de 20 números generados aleatoriamente entre 1 y 35, y utilizamos el for para imprimir los primeros 10 números de la lista.
# ?????????????????
'''
from random import randint # random int
a = []
for i in range(20):
    a.append(randint(1,35))

print("** a -->",a, end=' ')
print()
print('Segunda Mitad: ')
for n in a[10:]:
    print(n, end=' ')
'''    
# el END formatea la salida
# print(i, end=' - ') // 0 - 1 - 2 - 3 - 4 -
''' 
print()
print('Primera Mitad:')
for n in a[:10]:
    print(n, end=' ')
print()
'''

# 1.6 Métodos de la secuencia str
# capitalize() Devuelve el string con la primera letra en mayúscula.
print("hola".capitalize())

# center(ancho[,relleno]) Devuelve el string centrado con relleno a los costados.
print("Python".center(10, "*"))

# count(valor) Devuelve la cantidad de veces que aparece "valor" en el string.
print("banana".count("a"))

# fi nd(substring[,desde[,hasta]]) Devuelve la primera posición de comienzo del substring en el string.
print("python".find("th"))

# rfi nd(substring[,desde[,hasta]]) Devuelve la última posición de comienzo del substring en el string.
print("python programming".rfind("ing"))

# format(args,*) Devuelve el string formateado con valores sustituidos.
print("Mi nombre es {} y tengo {} años".format("Juan", 25))

# upper() Devuelve el string en mayúsculas.
print("hola".upper())

# lower() Devuelve el string en minúsculas.
print("Hola".lower())

# strip() Devuelve el string sin espacios en blanco al inicio y al fi nal.
print(" Python ".strip())

# replace(viejo, nuevo) Devuelve el string con todas las apariciones de "viejo" reemplazadas por "nuevo".
print("Hello, World!".replace("Hello", "Hi"))

# split([separador]) Devuelve una lista de substrings separados por "separador".
print("apple,banana,grape".split(","))

# join(iterable) Devuelve un string que es la concatenación de los elementos en el iterable.
print(",".join(["apple", "banana", "grape"]))

# isdigit() Devuelve True si todos los caracteres son dígitos.
print("12345".isdigit())

# isalpha() Devuelve True si todos los caracteres son letras.
print("Python".isalpha())

# startswith(substring) Devuelve True si el string comienza con "substring".
print("Hello, World!".startswith("Hello"))

# rindex(substring[,desde[,hasta]] ) Devuelve la última posición de comienzo del substring en el string.
print("python programming".rindex("ing"))

# join(iterable) Devuelve un string que es la concatenación de los elementos en el iterable, intercalados con el string.
print("Python".ljust(10, "-"))

# ljust(ancho[,relleno]) Justifica el string hacia la izquierda con relleno.
print("Python".ljust(10, "-"))

# ljust(ancho[,relleno]) Justifica el string hacia la derecha con relleno.
print("Python".rjust(10, "-"))

# maketrans(x[,y[,z]]) Asocia # en un diccionario los correspondientes caracteres de las cadenas x e y.
print(str.maketrans("aeiou", "12345")) 

# Devuelve el string con los caracteres asociados en el diccionario pares reemplazados.
print("hello".translate(str.maketrans("aeiou", "12345")))










