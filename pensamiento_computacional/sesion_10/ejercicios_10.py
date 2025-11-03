# GUIA DE EJERCICIOS Nº6 – Pandas
import pandas as pd

# print(pd.__version__)  # 2.3.3
"""
Los siguientes ejercicios se pueden hacer en el siguiente link de Google Colab:
https://colab.research.google.com/drive/1onufzB7CnauWQFHuMMrDQxXkevqCGeAj?usp=sharing

"""
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

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# df = pd.DataFrame(peliculas)
df = pd.DataFrame(peliculas, index=labels)
print(df)


# ============================================================
# ✅ 1. Mostrar la información del DataFrame con el método info()
"""
¿Cómo se llaman y qué tipo de dato tiene cada columna?
¿Cuántos elementos nulos hay en cada columna?
Interpretar qué información se guarda en esta tabla y para qué puede servir.
"""
# ============================================================
print()
print("df.info() 🔽")
print(df.info())


# ============================================================
# ✅ 2. Mostrar sólo los nombres de las primeras 3 películas del DataFrame.
# ============================================================
print()
print("df.head(3) 🔽")
print(df.head(3))

# ============================================================
# ✅ 3. Mostrar sólo el director y el género de todas las películas.
# ============================================================

print()
print("df[['director', 'género']] 🔽")
print(df[['director', 'género']])

print()
print("df.loc[:, ['director', 'género']] 🔽")
print(df.loc[:, ['director', 'género']])

# ============================================================
# ✅ 4. Mostrar las películas que sean de drama.
# ============================================================

print()
print("df[df['género'] == 'drama'] 🔽")
print(df[df['género'] == 'drama'])

# ============================================================
# ✅ 5. ¿Qué cantidad de películas hay de cada género?
# ============================================================

print()
print("df.groupby('género').count() 🟡")
print(df.groupby("género").count())

# Esto muestra los géneros distintos que hay.
print()
print("df.groupby('género').count() 🟡")
print(df.groupby("género").count())

# # value_counts agrupa y cuenta cada valor de la columna 'género'. Ordena de mayor a menor segun los valores obtenidos
print()
print("df['género'].value_counts()) 🟢")
print(df["género"].value_counts())

# agrupa el DataFrame por 'género' y luego cuenta cuántas filas hay en cada grupo.
print()
print("df.groupby('género')['género'].count()) 🟢")
print(df.groupby('género')['género'].count())

# ============================================================
# ✅ 6. Mostrar las películas que tengan puntaje entre 6 y 8 y cuyo año de estreno sea anterior a los 2000.
# ============================================================

print()
print("df[df['puntaje'].between(6, 8) & (df['año'] < 2000)] 🟢")
print(df[df["puntaje"].between(6, 8) & (df["año"] < 2000)])

# ============================================================
# ✅ 7. Mostrar las películas que no hayan sido puntuadas
# (que el puntaje tenga un valor nulo).
# ============================================================

print()
print("df[df['puntaje'].isnull()] 🟢")
print(df[df["puntaje"].isnull()])


# ============================================================
# ✅ 8. Calcular el promedio del puntaje de todas las películas.
# ============================================================

print()
print("df.groupby('género')['género'].mean() 🟢")
print(df.groupby('género')['puntaje'].mean())

# ============================================================
# ✅ 9. Ordenar las películas en orden alfabético descendente.
# ============================================================

print()
print("df.sort_values(by=['nombre']) 🟢")
print(df.sort_values(by=["nombre"]))

# ============================================================
# ✅ 10. Mostrar las 3 películas más antiguas.
# ============================================================

print()
print("df.sort_values(by='año').head(3) 🟢")
print(df.sort_values(by="año").head(3))

# ============================================================
# ✅ 11. Mostrar sólo el nombre y el año de las 3 películas más nuevas.
# ============================================================

print()
print("df[['nombre', 'año']].sort_values(by='año', ascending=False).head(3) 🟢")
print(df[["nombre", "año"]].sort_values(by="año", ascending=False).head(3))

# ============================================================
# 12. Agregar una columna que indique si la película fue vista, o no. Una película fue vista cuando tiene puntaje no nulo.
# ============================================================

print()
print("df['fue_vista'] = df['puntaje'].notnull()  🟢")
df["fue_vista"] = df["puntaje"].notnull() 
print(df)

print()
print("df['fue_vista'] = df['puntaje'].notnull().map({True: 'Sí', False: 'No'}) 🟢")
df["fue_vista"] = df["puntaje"].notnull().map({True: "Sí", False: "No"})
print(df)


