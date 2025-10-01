from random import randint # random int

# Secuencias, tuplas y listas Unidad 4

# Familiarización con secuencias
# ✅ 1. Crear una lista con los números del 1 al 10. Acceder con el índice a la posición que contiene el número 5, e imprimirlo por pantalla. Recordar que el índice de las listas empiezan con 0.

# ❗Un objeto range es una secuencia inmutable de números que se usa comúnmente en bucles, pero no es una lista en sí misma. list(range())
# ❌ Esto así: list_01 = [list(range(1, 11))] da: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]] NO quiero eso
# list_01 = list(range(1, 11)) # 1 - 10 | ÍNDICES 0 - 9
# print("list_01[4] -->", list_01[4])

# 2.✅ Con la lista del punto anterior, usar la función len() para averiguar su longitud, e imprimirla.
# print("len(list_01) -->", len(list_01))

# 3. Crear una secuencia con números distintos, y luego devolver el elemento máximo y el mínimo.
"""
tupla_03 = []
tupla_03_bis = ()
for i in range(0, 15):
    tupla_03.append(randint(1,35))
print("tupla_03 -->", tupla_03)
print("min(tupla_03) -->", min(tupla_03))
print("max(tupla_03) -->", max(tupla_03))
"""


# 4. Ordenar la secuencia del ejercicio anterior, e imprimirla por pantalla. (ver funciones de listas)
# tupla_03_ordenada = sorted(tupla_03)
# print("tupla_03_ordenada -->", tupla_03_ordenada)

# 5. Crear una tupla que guarde tu nombre y tu edad. Luego, imprimir por pantalla tu edad, accediendo al elemento de la tupla que corresponda.
# tupla_05 = ('Victoria', 20)
# print("tupla_05[1] -->", tupla_05[1])

# 6. Hacer una lista con 5 nombres, y realizar las siguientes actividades con la misma:
"""
a. Cambiar el último elemento de la lista y cambiar el último nombre por "Juan". Olvidándonos de que sabemos que tiene 5 elementos, ¿Cómo podría saber cuál es el último elemento si no sé la longitud? [-1]
b. Devolver el nombre que esté a dos posiciones del final. ¿Cómo hacemos para que nos funcione para cualquier lista y no solo para la que tenga 5 elementos? [-2]
c. Recorrer la lista e imprimir cada nombre por pantalla.
d. Imprimir por pantalla la lista con 3 repeticiones, usar el operador repetición (*).
"""
# a
"""
lista_nombres = ['Victoria', 'Leandro', 'Lucila', 'Agustin', 'Micaela']
lista_nombres[-1] = 'Juan'
print(lista_nombres[-1])
# b
lista_nombres[-2]
print(lista_nombres[-2])
# c
for name in lista_nombres:
    print("name",name)
# d
print(lista_nombres*3) # ['Victoria', 'Leandro', 'Lucila', 'Agustin', 'Juan', 'Victoria', 'Leandro', 'Lucila', 'Agustin', 'Juan', 'Victoria', 'Leandro', 'Lucila', 'Agustin', 'Juan']
"""

# 7. Se pide ahora crear 3 tuplas como las del ejercicio 5, con un nombre y una edad. A continuación, guardarlas en una lista. Pensar, ¿De que nos servirá guardar las tuplas en una lista en vez de tenerlas por separado?

# ej_07 = [('Victoria', 20), ('Victoria', 20), ('Victoria', 20)]

# Ejercicios con listas y tuplas
# 8. Se quiere guardar información de los siguientes países: Francia, Argentina, Japón, Alemania, Perú.
"""
a. Crear una tupla para cada país que contenga su nombre, su capital y el continente donde se encuentra.
b. Guardar las tuplas en una lista.
c. Hacer una función que reciba por parámetros la lista, e imprima la información de cada país con el siguiente formato: País: <nombre> Capital: <capital> Continente: <continente>
Por ejemplo:
País: Japón
Capital: Tokio
Continente: Asia
"""

"""
Francia = ('Francia', 'Paris', 'Europa') 
Argentina = ('Argentina', 'Buenos Aires', 'America del Sur') 
Japón = ('Japón', 'Tokio', 'Asia') 
Alemania = ('Alemania', 'Berlín', 'Europa') 
Perú = ('Perú', 'Lima', 'America del Sur') 
lista_paises = [Francia, Argentina, Japón, Alemania, Perú]

def ej_08(listaPaises):
    for pais in listaPaises:
        print(f'País: {pais[0]}, Capital: {pais[1]}, Continente: {pais[2]}')
ej_08(lista_paises)
"""

# 9. Una librería tiene un sistema que guarda los nombres de todos los libros que tienen en una lista de la siguiente forma: ["El principito", "It", "Sherlock Holmes"...]. Se quiere saber cuántos libros repetidos tienen. Hacer código que imprima para cada título, cuántos ejemplares hay.
# Aclaración: No se sabe la cantidad de elementos que tiene la lista, la lista nombrada es solo un ejemplo.
libros_libreria = ["El principito", "It", "Sherlock Holmes", "It"]
def ej_09(libroLibreria):
    lista_formateada = []
    encontrado = False
    for listalibros in libroLibreria:
        
            if(libroLibreria.count(listalibros) == 1):
                print("--- if", listalibros)
                lista_formateada.append((listalibros, libroLibreria.count(listalibros)))
                
            if(libroLibreria.count(listalibros)>1):
                for i in lista_formateada:
                    if(i[0] == listalibros):
                        encontrado = True   # Ya está, no lo agrego de nuevo
                        break
                if not encontrado:
                    lista_formateada.append((listalibros, libroLibreria.count(listalibros)))    
    print("--- lista_formateada", lista_formateada)
ej_09(libros_libreria)


# 10. Crear una lista que contenga los números del 1 al 10, luego recorrerla y guardar en otra lista esos números elevados al cuadrado.
"""
lista_10 = range(1, 11)
lista_cuadrados = []
for i in lista_10:
    lista_cuadrados.append(i**2)
print("lista_cuadrados", lista_cuadrados)
"""

# 11. Se tiene la siguiente lista de palabras: ["entender", "pueden", "humanos", "los", "que", "código", "escriben", "programadores", "buenos", "Los", "entiende.", "computadora", "una", "que", "código", "escribe", "tonto", "Cualquier"]. 
# Hacer una función que reciba una lista, y devuelva un string uniendo las palabras desde el final de la lista hasta el principio con un " " (espacio) entre cada una, para formar la frase. (ver funciones de listas y strings).
lista_11 = ["entender", "pueden", "humanos", "los", "que", "código", "escriben", "programadores", "buenos", "Los", "entiende.", "computadora", "una", "que", "código", "escribe", "tonto", "Cualquier"]
"""
def ej_11(lista_palabras):
    lista = lista_palabras[::-1]
    lista = " ".join(lista)
    print("lista",lista)
    return lista
ej_11(lista_11)

# Con reverse
def ej_11(lista_palabras):
    lista_palabras.reverse()
    lista = " ".join(lista_palabras)
    print("lista",lista)
    return lista
ej_11(lista_11)
"""

# 12. Se quiere hacer un sistema en la facultad para que un alumno pueda ir guardando las materias que va haciendo. Para eso, crear una función que le pregunte al usuario la materia que quiere almacenar, e ir guardando la información en una lista hasta que ingrese una ‘X’. ¿Qué funciones de listas no permiten insertar en una lista?

# 13. Se tiene un ticket de supermercado que se puede representar como una lista de tuplas (producto, precio).
"""
a. Hacer una función que reciba la lista, calcule y devuelva el total que hay que pagar.
b. Ahora se tienen dos tickets. Juntar ambos y volver a calcular el total.
Un ejemplo de lista puede ser: [("Detergente", 123), ("Jabón Líquido", 456)] y nos tendría que devolver 579. (No copien y peguen la lista de la guía, porque hay caracteres que no los va a reconocer el editor de texto).
"""









