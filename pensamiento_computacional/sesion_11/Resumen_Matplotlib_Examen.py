# ============================================================
# 🧠 RESUMEN MATPLOTLIB - PENSAMIENTO COMPUTACIONAL
# ============================================================

import matplotlib.pyplot as plt
import pandas as pd

# --- Gráfico básico ---
x = [0,2,10,11,18,25]
y = [0,1,2,3,4,5]

fig, ax = plt.subplots()
ax.plot(x, y, color='green', marker='^', linestyle='--', linewidth=2.2)
ax.set_title("Gráfico de posición")
ax.set_xlabel("Tiempo (min)")
ax.set_ylabel("Distancia (m)")
ax.grid(axis='y', color='gray', linestyle='dashed')
plt.show()

# --- Tipos de gráficos ---
ax.scatter(x, y)
ax.bar(['A','B','C'], [10,20,15])
ax.barh(['A','B','C'], [10,20,15])
ax.pie([40,30,30], labels=['A','B','C'], autopct='%1.1f%%')
plt.show()

# --- Gráficos múltiples ---
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(x, y, color='blue')
ax[1].scatter(x, y, color='red')
plt.show()

# --- Ejemplo con DataFrame ---
data = {'animal': ['gato','perro','serpiente'], 'edad': [2,7,3]}
df = pd.DataFrame(data)

fig, ax = plt.subplots()
ax.bar(df['animal'], df['edad'])
ax.set_title("Edad de mascotas")
ax.set_ylabel("Años")
plt.show()

# --- Ejemplo con dataset gapminder ---
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
