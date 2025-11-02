import pandas as pd

peliculas = {
    "nombre": [
        "Titanic",
        "Kil Bill",
        "Matrix",
        "El padrino",
        "Avatar",
        "Casablanca",
        "El exorcista",
        "Soy leyenda",
        "El club de la pelea",
        "Mujercitas",
    ],
    "director": [
        "James Cameron",
        "Quentin Tarantino",
        "Hermanas Wachowski",
        "Francis Ford Coppola",
        "James Cameron",
        "Michael Curtiz",
        "William Friedkin",
        "Francis Lawrence",
        "David Fincher",
        "Greta Gerwig",
    ],
    "año": [1997, 2003, 1999, 1972, 2009, 1942, 1973, 2007, 1999, 2019],
    "género": [
        "romance",
        "acción",
        "ciencia ficción",
        "drama",
        "ciencia ficción",
        "drama",
        "terror",
        "ciencia ficción",
        "drama",
        "drama",
    ],
    "puntaje": [8.6, None, 6.9, 7.5, 9.1, 6.0, None, None, 9.4, 8.0],
}

# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# df = pd.DataFrame(peliculas)
df = pd.DataFrame(peliculas, index=labels)
# df

# [desde:hasta:salteando]
# DESDE - SIN INCLUIR
# HASTA - INCLUIDO
print(df.iloc[3:]) # desde el 3 SIN INCLUIR


df.iloc[6:8] # Desde el 6 sin incluir, hasta el 8 incluido

df.info()# entries significa filas
# Dtype trata de inferir el tipo de dato. Pero si no puede, porque son distintos; dice object.

df.head(3) # Devuelve las primeras (n) filas que se le pase por parametro
# Si no se le pasa ningun valor, devuelve las primeras 5
df.head(23) # Si le paso una cantidad que no tiene, me devuelve el total de elementos que tenga

df.describe()

# df.loc[[filas],[columnas]]
# IMPORTANTE, si no voy a filtrar ninguna FILA, debo poner [:, [columnas]]

# Indico filas y columnas
df.loc[[5, 8], ['nombre', 'año']]

# Si el indice fueran letras u otra cosa. Podria decir: Mostrar fila 3, 4 y 5
# df.loc[df.index[[3, 4, 8], ['nombre', 'año']]]

# ⚠ Hasta ahora no estaba filtrando por el contenido de la tabla

# Preguntar si una columna es nula/NaN con isnull()
# DEVUELVE LAS QUE TIENEN VALOR NULO, en la columna que le estoy pidiendo
df[df['puntaje'].isnull()]

# .isnull() == False ---> Me devuelve todas las que no son NaN
# .isnull() devuelve True si encuentra NaN. Si devuelve False, es porque no es Nan
df[df['puntaje'].isnull() == False]

# Las condiciones pueden ser tan complejas como uno quiera
# Los operadores son DISTINTOS
# OR ---> |
# AND ---> &
# NOT ---> ~

df[(df['género'] == 'drama') & (df['puntaje'] >= 8) ]

# Funcion between. Incluye ambos extremos
df[df['puntaje'].between(8.6, 9.4)]

# CAMBIAR INFO DEL DATA FRAME
# asigno un nuevo valor a una columna y fila especifica
df.loc[[5], 'puntaje'] = 11
df.loc[[5], 'puntaje']

# La funcion sum() suma todos los valores de la columna seleccionada
df['puntaje'].sum()
df['género'].sum()

# groupby
# Agrupa las filas por los valores de la columna género
# Y con la funcion .mean() devuelve el valor del promedio del puntaje
df.groupby('género')['puntaje'].mean()

# AGREGAR Y QUITAR FILAS/ELEMENTOS AL DATA FRAME
df.loc[11] = ['Maze runner', 'James dashner', 2012,'Distopía',10]
df.drop(10)

# value_counts devuelve cuantas veces aparece cada valor único para una columna especifica
df['género'].value_counts()

# sort_values(by, ascending)
# ordena la tabla con el criterio que se pide
# by: LISTA con las COLUMNAS a usar para ORDENAR
# ascending: LISTA de Booleanos para indicar si es ascendente o no el orden
df.sort_values(by=['género'], ascending=[False])

# filter permite achicar la lista
# map permite transformar los elementos de la lista
# en pandas, permite transformar los elementos del df
# lo que encuentre con 'yes' lo va a transformar a TRUE
# df['priority'] = df['priority'].map({'yes': True, 'no': False})

# reemplaza el 1er parametro, por el 2do
df['género'] = df['género'].replace('Distopía', 'distopía')

