
![alt text](image.png)

# Pandas
Es una biblioteca. 
Se utiliza para el análisis y la manipulación de datos. Ayuda a los usuarios a limpiar, transformar y analizar datos de una manera rápida y eficiente.
La estructura de datos principal en Pandas se llama `DataFrame`. Es una tabla de datos bidimensional que se compone de filas y columnas, y se asemeja a una tabla relacional.

## Filtrar filas: `df.iloc()` y `df.head()`
```py
# Devuelve las primeras (n) filas que se le pase por parametro
# Si no se le pasa ningun valor, devuelve las primeras 5
df.head(n)  

# DESDE - SIN INCLUIR
# HASTA - INCLUIDO
df.iloc([desde:hasta:salteando])
```

## Filtrar filas y columnas `df.loc[[filas],[columnas]]`
### IMPORTANTE, si no voy a filtrar ningún FILA, debo poner [:, [columnas]]
```py
df.loc[:,['nombre', 'año']]
```

# Indico filas y columnas
### Para las filas: [desde:hasta:salteando]
```py

df.loc[[5, 8],['nombre', 'año']]

# Esto tambien es válido
df.loc[[5, 8]]

```


- https://colab.research.google.com/drive/1qANZCP0wA67A8S1rt2HSAqBar-RCXTDM#scrollTo=SfV8of8i9nRy
- https://www.w3schools.com/python/pandas/pandas_getting_started.asp
# PIP is a package manager for Python packages, or modules if you like.
- https://www.w3schools.com/python/python_pip.asp
- https://youtu.be/ZlMNodo0OMw?si=wb6nY5kU9V1qs5bT
- https://www.geeksforgeeks.org/pandas/python-pandas-dataframe-groupby/
- https://www.w3schools.com/python/pandas/ref_df_groupby.asp
- https://4geeks.com/es/how-to/anadir-columna-dataframe-python
- https://www.geeksforgeeks.org/pandas/adding-new-column-to-existing-dataframe-in-pandas/

