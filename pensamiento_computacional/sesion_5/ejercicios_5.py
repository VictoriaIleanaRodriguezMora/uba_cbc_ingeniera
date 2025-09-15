# Recursos con Strings
# 1. Hacer una función que reciba un string y que imprima solamente los caracteres que sean vocales.
"""
def ej_01(string):
    final_string = ''
    vocales = ['a', 'e', 'i', 'o', 'u']
    # string.replace(vocales, '')
    for letra in string:
        for i in vocales:
            if (letra == i):
                final_string += letra
    print("string", string)
    print("final_string", final_string)
    
ej_01('Hola que tal')
"""

# 2. Hacer una función que reciba un string y que lo invierta.
"""
def ej_02(string):
  
    print("string[::-1]", string[::-1])

ej_02('Hola que tal')
"""

# 3. Hacer una función que reciba dos strings, un string y un substring, es decir, que el primero contiene al segundo, se pide devolver el string habiendo eliminado el substring del mismo.
"""
Ejemplo:
string: "Campeones del Mundo - 2022"
substring: "2022"
Una vez llamada a la función el string nos debería quedar "Campeones del Mundo - ",
notar que solo borra el año, el espacio no.
"""
"""
def ej_03(string, substring):
  
    print("string.replace(substring, '')", string.replace(substring, ''))

ej_03('Campeones del Mundo - 2022', '2022')
"""

# Recursos con listas
# Para todos estos ejercicios se recomienda fuertemente tener a mano la documentación de los métodos de listas.
# 4. Un chef está armando una lista de supermercado con todos los ingredientes que hay que comprar. Sólo quiere agregar un ingrediente a la lista si no lo escribió antes, así no tiene repetidos. Hacer un programa que inserte un nuevo elemento en una lista de strings, solamente si el elemento que se desea insertar no se encuentra en la lista. La lista de ingredientes la podemos pensar como una lista de strings.
"""
Ejemplo:
ingredientes: ["tomate", "queso", "cebolla", "huevo"]
ingrediente a agregar: "orégano"
La lista de ingredientes debería quedar ["tomate", "queso", "cebolla", "huevo", "orégano"]
En cambio, si el ingrediente a agregar es "queso" la lista debería quedar igual.
"""
"""
lista_ingredientes = ["tomate", "queso", "cebolla", "huevo"]
def ej_04(lista, agregar):

    if(agregar in lista):
        print("está en la lista")
    else:
        lista.append(agregar)
    
    print("lista", lista) # lo muestra siempre

ej_04(lista_ingredientes, "orégano")
ej_04(lista_ingredientes, "queso")
"""

# 5. Agustina está jugando a las cartas con sus amigos. A ella le gusta tener las cartas de su mano bien ordenadas. Esto significa que cada vez que tiene que agarrar una nueva carta, la quiere agregar a su mano en el lugar indicado para no romper el orden. 

# Si se tiene una lista de enteros ordenadas de mayor a menor. Hacer una función que según esta lista inserte un nuevo entero, manteniendo el orden. 
# Podemos pensar la lista de cartas como números enteros. Ejemplo: cartas: [1, 4, 6, 8] carta nueva: 5 La lista de cartas debería quedar: [1, 4, 5, 6, 8] 
# Tratar de pensar una solución sin usar el método sort. (no es obligatorio).



# 6. Santiago armó una lista con el pedido de empanadas de su familia pero ahora quiere saber la cantidad de gustos diferentes que tiene que pedir. Podemos pensar la lista de empanadas como una lista de strings, entonces deberíamos devolver la cantidad de strings diferentes que hay en una lista.
# 7. Manuel y su pareja armaron una lista numerada con las actividades de mantenimiento de la casa. Decidieron dividirse las tareas, a Manuel le tocó hacer todas las actividades con número par, por eso necesitamos hacer una función que reciba una lista de enteros, y devuelva otra lista que solamente contenga números pares, que vienen a ser las tareas de Manuel.






