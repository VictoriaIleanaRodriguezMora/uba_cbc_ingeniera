# Tuplas

tupla_vacia = () # tupla_vacia
print("tupla vacía: ", tupla_vacia) # ()

lista_vacia = [] # lista_vacia
print("lista vacía: ", lista_vacia) # []

tupla_1 = ("Pensamiento")
print("tupla 1: ", tupla_1) # Pensamiento
tupla_1_bis = ("Pensamiento",)
print("tupla 1_bis: ", tupla_1_bis) # 'Pensamiento',)

lista_1 = ["Pensamiento"]
print("lista 1: ", lista_1) # Pensamiento
lista_1_bis = ["Pensamiento",]
print("lista 1_bis: ", lista_1_bis) # 'Pensamiento',)

tupla_con_elementos = ("Pensamiento", 90, 'a', [1, 2]) # Contiene una lista
print("tupla_con_elementos: ", tupla_con_elementos) #  ('Pensamiento', 90, 'a', [1, 2])

lista_con_elementos = ["Pensamiento", 90, 'a', [1, 2]] # Contiene una lista
print("lista_con_elementos: ", lista_con_elementos) #  ['Pensamiento', 90, 'a', [1, 2]]

# La posicion se marca igual en tuplas y listas
print("tupla_con_elementos[0]",tupla_con_elementos[0])
print("lista_con_elementos[0]",lista_con_elementos[0])

# Desestructuración. Es igual en tuplas y listas
fecha = (12, "Junio", 1970)
print(fecha);
# 0,  1 ,  2 
dia, mes, anio = fecha # Desestructura por posiciones
print("dia ", dia, "mes ", mes, "anio ", anio)

# Una lista de tuplas
puntos = [
    (4, 6),
    (8, 2),
    (10, 5),
    (1, 1),
    (0, 0),
]

# append - agregar elementos al final
puntos.append((99, 99))

# insert(posicion, valor). Mueve todo el arreglo, para insertar en la posicion que yo le digo
puntos.insert(5, (88, 88))

# puntos.remove((elemento a borrar)) - tiene que existir 
puntos.remove((0, 0))

for punto in puntos:
    # Punto es la posicion 0, 1, ... de puntos
    x, y = punto # x, y es la desestructuracion de la posicion[0], posicion[1]
    print("x: ", x, "y: ", y)

# Todo esto se puede hacer, porque estoy manipulando una lista. Las listas son mutables. Esto no lo podria hacer con una tupla. 
