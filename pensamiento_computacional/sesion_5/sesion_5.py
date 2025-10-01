personas = [
    ("Manola Bellido Mur", 34),
    ("Segismundo Andreu Maldonado", 21),
    ("Anselma Arregui-Solano", 67),
    ("Candelas Perelló Marqués", 23),
    ("Itziar Flores Viana", 87),
    ("Armida Peinado Jaén", 34),
    ("Cecilia del Vilaplana", 67),
    ("Mayte Amador Lamas", 99),
    ("Heliodoro Serra Cases", 28),
    ("Lope Orozco", 46)
]

resultado = ("Cecilia del Vilaplana", 67) in personas
print(resultado)

resultado2 = personas.index(("Anselma Arregui-Solano", 67)) # posicion 2
# si no existe devuelve error
print(resultado2)

# sort recibe 2 parametros. modifica la funcion original, por eso:
# print(personas.sort()) # devuelve none

# Ordena por el primer parametro. Que es caracter, y ordena alfabeticamente
personas.sort() 
print("personas.sort()", personas)
print()

# personas.sort(reverse=True) 
personas.sort(reverse=True) # Del ya ordenado, lo muestra al reves
print("personas.sort(reverse=True)", personas)
print()


def ordenarPorEdad(persona):
    return persona[1]


# Ordeno por medio de una funcion que yo le indico
personas.sort(key=ordenarPorEdad) 
print()
personas.sort(key=ordenarPorEdad,reverse=True) 
print("personas.sort(key=ordenarPorEdad) ", personas)

# .map y filter
# map(funcion_a_aplicar, secuencia) | filter(funcion_a_aplicar, secuencia)
# Filter --> Dada una secuencia, puedo filtrar elementos por una condicion

def cortar_palabra(palabra):
    return palabra[:4] # desde 0 hasta 4

# esto es una tupla
palabras = (
    "mesa",
    "silla",
    "ventana",
    "puerta",
    "auto",
    "pileta",
    "plantas"
)
# palabras_cortas 
# map va a operar,aplicar sobre todos los elementos de palabras la funcion cortar palabra. map retorna una nueva lista con lo que hace la funcion del primer parametro, entonces lo guardo en la misma linea
palabras_cortas = map(cortar_palabra, palabras) 
print("palabras_cortas", palabras_cortas) # <map object at 0x0000018AFF350B50>
print("list(palabras_cortas)", list(palabras_cortas)) # ['mesa', 'sill', 'vent', 'puer', 'auto', 'pile', 'plan']
print("palabras", palabras) # ('mesa', 'silla', 'ventana', 'puerta', 'auto', 'pileta', 'plantas')

# map no modifica el arreglo original, genera un nuevo mapa. para poder interpretar el mapa, le digo que lo trate como un list() o tuple()

def es_palabra_corta(palabra):
    if( len(palabra) < 5):
        return True
    else:
        return False

# Todas las funciones que se usan en filter tienen que devolver True o False 
palabras_cortas_2 = filter(es_palabra_corta, palabras) 
print("palabras_cortas_2", palabras_cortas_2) # <filter object at 0x00000219E3AE1030>
print("palabras_cortas_2", list(palabras_cortas_2)) # ['mesa', 'auto']



