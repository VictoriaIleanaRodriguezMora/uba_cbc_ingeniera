- https://colab.research.google.com/drive/11JNlC78bR8_ZR_LWnX-FsKOj-7AcL740

# Matplotlib – Cheatsheet 

## 📦 Importación y estructura básica
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()   # Crea figura y ejes
plt.show()                 # Muestra el gráfico
```

---

## Tipos de gráficos

| Tipo                | Función                                                | Descripción                    |
| ------------------- | ------------------------------------------------------ | ------------------------------ |
| Línea               | `ax.plot(x, y)`                                        | Muestra evolución o tendencia  |
| Puntos              | `ax.scatter(x, y)`                                     | Relación entre variables       |
| Barras              | `ax.bar(x, y)`                                         | Comparar proporciones          |
| Barras horizontales | `ax.barh(x, y)`                                        | Barras horizontales            |
| Torta               | `ax.pie(valores, labels=etiquetas, autopct='%1.1f%%')` | Porcentajes o partes del total |

---

## Personalización

```python
ax.set_title("Título del gráfico")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.legend()                # Muestra referencias
ax.grid(True)              # Agrega cuadrícula
ax.set_xlim(0, 10)         # Límite eje X
ax.set_ylim(0, 100)        # Límite eje Y
```

**Parámetros comunes**
- `color='green'`, `marker='^'`, `linestyle='--'`, `linewidth=2.2`
- `markersize=8` → tamaño del marcador
- `linestyle` puede ser `'solid'`, `'--'`, `':'`, `'-. '` etc.

---

## Gráficos múltiples

```python
fig, ax = plt.subplots(2, 2, figsize=(10, 8))
ax[0, 0].plot(x, y, color='green')
ax[0, 1].scatter(x, y, color='red')
ax[1, 0].bar(x, y)
ax[1, 1].pie([40, 30, 30], labels=['A','B','C'])
plt.show()
```

---

## Ejemplo con DataFrame

```python
import pandas as pd

data = {'animal': ['gato','perro','serpiente'], 'edad': [2,7,3]}
df = pd.DataFrame(data)

fig, ax = plt.subplots()
ax.bar(df['animal'], df['edad'])
ax.set_title("Edad de las mascotas")
ax.set_ylabel("Años")
plt.show()
```

---

## Ejemplo con dataset Gapminder

```python
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv"
data = pd.read_csv(url)
data['year'] = data['year'].astype(int)

data_year = data[data["year"] == 2007]
plt.scatter(data_year["gdpPercap"], data_year["lifeExp"], color="#23A763", marker='^')
plt.title("Relación entre PBI per cápita y expectativa de vida (2007)")
plt.xlabel("PBI per cápita")
plt.ylabel("Expectativa de vida")
plt.grid()
plt.show()
```

---

- Usar `plt.subplots()` para gráficos complejos.  
- Siempre llamar `plt.show()` al final.  
- Recordar `plot` = línea, `scatter` = puntos, `bar` = barras, `pie` = torta.  
- Usar `ax.grid()` y `ax.legend()` para mejorar legibilidad.  
