# Los diccionarios son mutables
# Los valores de los diccionarios son mutables y pueden ser de cualquier tipo de dato. Pero la clave debe ser inmutable. 

diccionario = {1: 'Hola', 2: 'chau'}
# Se accede por la clave
# print(diccionario) # {1: 'Hola', 2: 'chau'}
# print(diccionario[1]) # Hola

# Quiero guardar el dato 'Hola', en la clave de acceso saludo_inicial
d_saludo = {"saludo_inicial": 'Hola', "saludo_final": 'Chau'}
# print(d_saludo)

# d_saludo no se reinicia, se agranda. Porque es mutable 
d_saludo['saludo_cumple'] = 'Feliz cumple!'
# print(d_saludo) # {'saludo_inicial': 'Hola', 'saludo_final': 'Chau', 'saludo_cumple': 'Feliz cumple!'}

amigos = {
    "Juan": (25, 'Marzo', 'Nos conocimos en la primaria'),
    "Ana": (28, 'Abril', 'Nos conocimos en la secundaria'), 
    "Pedro": (30, 'Diciembre', 'Nos conocimos en la facultad'),
    "Maria": (26, 'Mayo', 'No recuerdo donde nos conocimos'),
}
# print(amigos.keys()) # dict_keys(['Juan', 'Ana', 'Pedro', 'Maria'])
# print(amigos.items()) # dict_items([('Juan', (25, 'Marzo', 'Nos conocimos en la primaria')), ])
# es un array con los items del diccionario

# Hacer modificaciones.
# update({}) - Recibe otro diccionario. Si la clave existe, modifica su valor. Sino, la crea.
amigos.update({'Maria': (26, 'Mayo', 'En el jardín')})
print(amigos['Maria']) # (26, 'Mayo', 'En el jardín')

# Es case sentive el update
amigos.update({'maria': (26, 'Mayo', 'En el jardín')})
print(amigos) # {'Juan': (25, 'Marzo', 'Nos conocimos en la primaria'), }