# GUIA DE EJERCICIOS Nº7 – Manejo de errores

# ============================================================
# 1. Se quiere hacer un programa para pedirle al usuario que ingrese un número entero,
# y en caso de que el valor ingresado no sea un número entero, mostrarle un mensaje apropiado.
"""
a) Realizarlo utilizando isnumeric().
   → isnumeric() sirve solo para strings que contienen dígitos (no acepta negativos ni decimales).
   → Limitación: no funciona con números negativos ni con valores tipo float.
b) Realizarlo utilizando try / except para capturar errores al convertir a int.
"""
# ============================================================


# ============================================================
# 2. Crear una función (usando el punto anterior) que le pida al usuario un número entero.
# Utilizarla para calcular el producto entre dos números enteros ingresados.
"""
Ejemplo:
Ingrese el primer número: 5
Ingrese el segundo número: 3
Resultado: 15
"""
# ============================================================


# ============================================================
# 3. Programa que solicite al usuario un número divisor y un dividendo,
# y calcule el cociente entre ellos.
"""
Ayuda:
- Considerar que el usuario podría ingresar un valor no numérico.
- También podría ingresar un divisor igual a 0 → debe manejarse el error de división.
"""
# ============================================================


# ============================================================
# 4. Crear un programa para abrir un archivo llamado “file.txt” en modo lectura.
# En caso de que este archivo no exista, mostrar el mensaje:
# “No se pudo encontrar el archivo file.txt”.
"""
Ayuda:
→ Usar try / except con FileNotFoundError.
"""
# ============================================================


# ============================================================
# 5. Crear una función cuyos parámetros sean una lista y un índice de posición
# para mostrar el valor de la lista en esa ubicación.
"""
a) ¿Qué ocurre si ingreso un índice fuera del rango?
   → Se genera un IndexError.
b) Si el índice está dentro del rango, mostrar el valor.
   Si está fuera, mostrar un mensaje apropiado.
"""
# ============================================================


# ============================================================
# 6. JUEGO DEL CHINCHÓN
# Para jugar con un único mazo de cartas españolas, el número de jugadores puede ser:
# 2, 3 o 4.
"""
Crear una función que pida al usuario el número de jugadores y contemple estos casos:
- Valor no válido (palabra o texto) → “Debe ingresar un número válido.”
- Valor menor a 2 → “Debe haber al menos 2 jugadores.”
- Valor mayor a 4 → “Se puede jugar con un máximo de 4 jugadores.”
- Valor válido → mostrar el número ingresado.
"""
# ============================================================


# ============================================================
# 7. JUEGO DEL TRUCO
# Para jugar con un único mazo de cartas españolas, el número de jugadores puede ser:
# 2, 4 o 6.
"""
Crear una función que pida al usuario el número de jugadores y contemple:
- Valor no válido (palabra o texto) → “Debe ingresar un número válido.”
- Valor menor a 2 → “Debe haber al menos 2 jugadores.”
- Valor mayor a 6 → “Se puede jugar con un máximo de 6 jugadores.”
- Valor impar (3 o 5) → “Debe haber un número par de jugadores.”
- Valor válido → mostrar el número ingresado.
"""
# ============================================================


# ============================================================
# 8. KIOSKO DE LA FACULTAD
"""
El kiosko quiere automatizar un cartel que calcule el total a pagar según el producto.

Se tienen dos diccionarios:
opciones = {
  1: "hamburguesas",
  2: "milanesas",
  3: "gaseosa",
  4: "alfajor",
  5: "papas fritas",
  6: "agua"
}

valores = {
  1: 1000,
  2: 1500,
  3: 500,
  4: 300,
  5: 600,
  6: 350
}

El programa debe:
1. Mostrar en pantalla los productos con sus precios, por ejemplo:
   1: hamburguesas -> 1000   2: milanesas -> 1500   3: gaseosa -> 500   4: alfajor -> 300   5: papas fritas -> 600   6: agua -> 350

2. Pedir al usuario una opción (código del producto) y una cantidad.

3. Imprimir el total a pagar.

Considerar posibles errores:
- Opción no numérica → mostrar “Debe ingresar un número válido.”
- Opción fuera del diccionario → mostrar “El código ingresado no existe.”
- En ambos casos, volver a pedir la opción hasta que sea válida.
"""
# ============================================================


