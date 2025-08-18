# Ejercicios sesión 2

# 1. Crear un programa que le solicite al usuario un entero y lo imprima por pantalla. Recordá que podés usar las funciones input (para solicitar información) y print para mostrar información

"""
valor = int(input("Ingrese un nro: "));
print(valor)
"""

"""
2. Crear un programa que le solicite al usuario dos números enteros y luego imprima por pantalla:
● la suma de ambos números
● la resta de ambos números
● la multiplicación de ambos números
● la división entera de ambos números
● el resto
// OUTPUT
Ingrese un nro: 5
Ingrese otro nro: 5
10
0
25
1.0
0
"""

"""
valorA = int(input("Ingrese un nro: "));
valorB = int(input("Ingrese otro nro: "));

print(valorA + valorB)
print(valorA - valorB)
print(valorA * valorB)
print(valorA / valorB)
print(valorA % valorB)
"""

# 3. ¿¿ Condicionales?? Crear un programa que le solicite al usuario un entero y determine si es par, mostrando por pantalla un mensaje que indique el resultado. Para determinar si un número es par o impar, se puede determinar con el uso del operador %, les dejamos a ustedes el cómo.
"""
valorC = int(input("Ingrese un nro: "));
print((valorC % 2)== 0)
"""

# 4. Escribir un programa que le pida a un usuario su año de nacimiento y otro año, y le diga qué edad tenía el usuario en el año ingresado
"""
def ejercicio_5(anio_nacimiento, otro_anio):
    calculo_edad = otro_anio - anio_nacimiento
    print(calculo_edad) # 10
    
ejercicio_5(2004, 2014)
"""

# 5. Crear un programa que le solicite al usuario 5 enteros y muestre por pantalla el promedio de ellos. Es muy común usar variables para acumular valores.
"""
def ejercicio_5(a, b, c, d, e):
    suma_valores = a+b+c+d+e
    promedio_valores = suma_valores / 5
    print(promedio_valores) # 3.0
    
ejercicio_5(1, 2, 3, 4, 5)
"""

# 6. Crear una función que reciba un número y muestre el anterior y el siguiente
"""
def ejercicio_5(num):
    num_anterior = num - 1
    num_siguiente = num + 1
    # 🔴 Usando f
    print(f"N° anterior: {num_anterior}, N° siguiente: {num_siguiente}") # 0 y 2
    
ejercicio_5(1)
"""

# 7. Crear una función que una un string y un entero, ambos dentro de un string.

# 8. a. Crear una función que reciba dos enteros y que retorne (devuelva) el resto de la división.
# b. Crear una función que reciba dos enteros y que retorne (devuelva) el cociente.

# 9. Pedirle nombre y apellido por separado e imprimir “Apellido, Nombre”. Este proceso se llama concatenar cadenas.
"""
def ejercicio_9(nombre, apellido):
    print(f"{apellido}, {nombre}") # Rodriguez, Victoria
    
ejercicio_9("Victoria", "Rodriguez")
"""

# 10. Obtener una palabra e imprimir la cantidad de letras.
"""
def ejercicio_10(palabra):
    print(f"{len(palabra)}") # 8
    
ejercicio_10("Victoria")
"""


# 11. Obtener una palabra e imprimir los primeros 5 caracteres (pista: slicear la palabra).
"""
def ejercicio_11(palabra):
    palabra_sliceada = palabra[0:5:1]
    print(palabra_sliceada) # Victo
ejercicio_11("Victoria")
"""
# ValueError: slice step cannot be zero


# 12. Obtener una palabra, borrarle todas las ‘a’ e imprimirla por pantalla (pista: usar una función predefinida de Python).
def ejercicio_12(palabra):
    palabra_modificada = palabra.replace("a", "")
    print(palabra_modificada) # Victoria
ejercicio_12("Victoria")
