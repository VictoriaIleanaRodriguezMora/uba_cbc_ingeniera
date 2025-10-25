# GUIA DE EJERCICIOS Nº4 – Recursos con Strings

# ============================================================
# 1. Hacer una función que reciba un string y que imprima solamente los caracteres que sean vocales.
# ============================================================

# """
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
# """

# ============================================================
# 2. Hacer una función que reciba un string y que lo invierta.
# ============================================================

# """
def ej_02(string):
  
    print("string[::-1]", string[::-1])

ej_02('Hola que tal')
# """

# ============================================================
# 3. Hacer una función que reciba dos strings, un string y un substring, es decir, que el primero contiene al segundo, se pide devolver el string habiendo eliminado el substring del mismo.
"""
Ejemplo:
string: "Campeones del Mundo - 2022"
substring: "2022"
Una vez llamada a la función el string nos debería quedar "Campeones del Mundo - ",
notar que solo borra el año, el espacio no.
"""
# ============================================================

# """
def ej_03(string, substring):
  
    print("string.replace(substring, '')", string.replace(substring, ''))

ej_03('Campeones del Mundo - 2022', '2022')
# """


# Recursos con listas

# ============================================================
# Para todos estos ejercicios se recomienda fuertemente tener a mano la documentación de los métodos de listas.
# 4. Un chef está armando una lista de supermercado con todos los ingredientes que hay que comprar. Sólo quiere agregar un ingrediente a la lista si no lo escribió antes, así no tiene repetidos. Hacer un programa que inserte un nuevo elemento en una lista de strings, solamente si el elemento que se desea insertar no se encuentra en la lista. La lista de ingredientes la podemos pensar como una lista de strings.
"""
Ejemplo:
ingredientes: ["tomate", "queso", "cebolla", "huevo"]
ingrediente a agregar: "orégano"
La lista de ingredientes debería quedar ["tomate", "queso", "cebolla", "huevo", "orégano"]
En cambio, si el ingrediente a agregar es "queso" la lista debería quedar igual.
"""
# ============================================================

# """
lista_ingredientes = ["tomate", "queso", "cebolla", "huevo"]
def ej_04(lista, agregar):

    if(agregar in lista):
        print("está en la lista")
    else:
        lista.append(agregar)
    
    print("lista", lista) # lo muestra siempre

ej_04(lista_ingredientes, "orégano")
ej_04(lista_ingredientes, "queso")
# """

# ============================================================
# 5. Agustina está jugando a las cartas con sus amigos. A ella le gusta tener las cartas de su mano bien ordenadas. Esto significa que cada vez que tiene que agarrar una nueva carta, la quiere agregar a su mano en el lugar indicado para no romper el orden. 

# Si se tiene una lista de enteros ordenadas de mayor a menor. Hacer una función que según esta lista inserte un nuevo entero, manteniendo el orden. 
# # Podemos pensar la lista de cartas como números enteros. 
# Ejemplo: cartas: [1, 4, 6, 8] carta nueva: 5 La lista de cartas debería quedar: [1, 4, 5, 6, 8] 
# Tratar de pensar una solución sin usar el método sort. (no es obligatorio).
# """
# ============================================================

lista_de_cartas = [1, 4, 6, 8]
#carta_nueva = 5
carta_nueva = 10
entro_al_else = False
for nro in lista_de_cartas:
    if(nro < carta_nueva):
        print(f"{nro} es menor a carta nueva {carta_nueva}")
    else:
        indice_nro_mayor = lista_de_cartas.index(nro) # posicion del nro que no es mayor a carta_nueva
        # print("indice_nro_mayor", indice_nro_mayor)
        lista_de_cartas.insert(indice_nro_mayor, carta_nueva)
        entro_al_else = True
        break # sin esto es un bucle infinito
# FUERA DEL BUCLE
if(entro_al_else == False): # si nunca entró en el else, significa que carta_nueva es mayor que todos
        lista_de_cartas.append(carta_nueva)

print("lista_de_cartas", lista_de_cartas)
# """

# ============================================================
# 6. Santiago armó una lista con el pedido de empanadas de su familia pero ahora quiere saber la cantidad de gustos diferentes que tiene que pedir. Podemos pensar la lista de empanadas como una lista de strings, entonces deberíamos devolver la cantidad de strings diferentes que hay en una lista.
# ============================================================

# """
lista_empanadas = ['Queso y cebolla', 'Jamón y queso', 'Calabresse', 'Calabresse', 'Jamón y queso', 'Carne', 'Queso y cebolla', 'Jamón y queso', 'Jamón y queso', 'Calabresse', 'Calabresse', 'Calabresse']
gustos_distintos = []
for gusto in lista_empanadas:
   if gusto not in gustos_distintos:
        gustos_distintos.append(gusto)
print('gustos_distintos',gustos_distintos)
print(f'Hay {len(gustos_distintos)} gustos distintos')
# """


# ============================================================
# 7. Manuel y su pareja armaron una lista numerada con las actividades de mantenimiento de la casa. Decidieron dividirse las tareas, a Manuel le tocó hacer todas las actividades con número par, por eso necesitamos hacer una función que reciba una lista de enteros, y devuelva otra lista que solamente contenga números pares, que vienen a ser las tareas de Manuel.
# ============================================================

lista_de_actividades = [1, 2, 3,4,5, 6,7,8]
actividades_manuel = []
for i in lista_de_actividades:
    if(i % 2 == 0):
        actividades_manuel.append(i)

print("actividades_manuel", actividades_manuel)


