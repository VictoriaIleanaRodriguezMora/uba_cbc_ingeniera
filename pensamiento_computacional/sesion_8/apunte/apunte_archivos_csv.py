completo = open('pensamiento_computacional/sesion_8/apunte/datosCompletos.csv', 'w') # Crea el archivo datosCompletos
b = [] # Crea la lista b vacía

# --- Procesar datos1.csv ---
dat = open('pensamiento_computacional/sesion_8/apunte/datos1.csv') # Abre datos1 sólo para lectura como dat
a = dat.readlines() # Carga en la lista a todas las líneas | un array donde cada string es una linea del archivo
dat.close() # Cierra archivo

for i in range(len(a)): # Rango de 0 al largo del array a
    a[i] = a[i].strip('\n') # Quita \n a cada línea
    a[i] = a[i].split(',') # Arma tabla quitando ; ¿?
    a[i][3] = int(a[i][3]) # A la columna 3 la convierte a entero
b = b + a # Agrega la lista 'a' a 'b'
print(a) # [['Luciana', 'juÃ¡rez', 'santiago del estero', 95],
# --- Procesar datos2.csv ---
"""
dat = open('pensamiento_computacional/sesion_8/apunte/datos2.csv') # Lo mismo que antes pero para datos2
a = dat.readlines()
dat.close()

for i in range(len(a)):
    a[i] = a[i].strip('\n')
    a[i] = a[i].split(',')
    a[i][3] = int(a[i][3])
b = b + a
"""

# --- Procesar datos3.csv ---
"""

dat = open('pensamiento_computacional/sesion_8/apunte/datos3.csv') # Lo mismo que antes pero para datos3
a = dat.readlines()
dat.close()

for i in range(len(a)):
    a[i] = a[i].strip('\n')
    a[i] = a[i].split(',')
    a[i][3] = int(a[i][3])
b = b + a
"""


# --- Ordenar y escribir ---
b.sort(reverse=True, key=lambda b: (b[3], b[2])) # Ordena la tabla b que tiene todas las filas de datos1, datos2 y datos3

# Imprimir el resultado ordenado en consola
for elemento in b:
    print(elemento) # Muestra las filas de b

# Escribir el resultado ordenado en el archivo
for elemento in b:
    elemento[3] = str(elemento[3]) # Para cada fila convierte columna 3 en texto
    ele = ';'.join(elemento) + '\n' # Arma string con separaciones de ; y agrega bajada de línea al final
    completo.write(ele) # Graba la línea en el archivo completo

completo.close()


