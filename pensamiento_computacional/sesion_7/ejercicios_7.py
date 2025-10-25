# GUIA DE EJERCICIOS Nº5 – Diccionarios

# ============================================================
"""
1. En una escuela se quiere tener un sistema para guardar la información de sus estudiantes para tener mejor organizado sus datos.
a. Crear un diccionario que sirve para representar a una persona en este contexto, pensar en las características que se consideren más relevantes para identificar a una persona (su nombre, DNI, edad, etc).
b. Agregar al diccionario creado, un campo que sea otro diccionario y sirva para guardar el curso del estudiante y sus características (año, división, orientación, etc).
c. Teniendo una lista de diccionarios de estudiantes, buscar en la lista la persona con mayor edad e imprimirla por pantalla.
"""
# ============================================================

print('Ejercicio 1')
# """
diccionario_alumno = {
    "dni": "12123456",
    "nombre": "",
    "ape": "",
    "edad": 18,
    "curso": {"anio": "5", "division": "A", "orientacion": "Naturales"},
}
lista_diccionarios_alumnos = [
    {
        "dni": "12123456",
        "nombre": "",
        "ape": "",
        "edad": 18,
        "curso": {"anio": "5", "division": "A", "orientacion": "Naturales"},
    },
    {
        "dni": "98652653",
        "nombre": "",
        "ape": "",
        "edad": 25,
        "curso": {"anio": "5", "division": "A", "orientacion": "Naturales"},
    },
    {
        "dni": "45689356",
        "nombre": "",
        "ape": "",
        "edad": 20,
        "curso": {"anio": "5", "division": "A", "orientacion": "Naturales"},
    },
]

# print(lista_diccionarios_alumnos)
largo_lista = len(lista_diccionarios_alumnos)  # 3

lista_ordenada = sorted(lista_diccionarios_alumnos, key=lambda alumno : alumno['edad'], reverse=True )
print('El estudiante de mayor edad tiene:', lista_ordenada[0]['edad'], 'años')
# """


# ============================================================
"""
2. En un vivero se guardan las plantas en una lista de diccionario con la siguiente información: especie, si necesita luz solar o no, y el precio. 
(OBSERVACIÓN: ¿Qué tipo de dato nos permitía guardar si algo es verdad o no?). 
Ahora se necesita un sistema que guarde las plantas a medida que van llegando. 
Se pide hacer una función que reciba la lista de diccionarios de plantas, y los datos de la planta nueva y agregue esa planta a la lista de diccionarios.
"""
# ============================================================

print('Ejercicio 2')
# """
a_plantas = [
    {"especie": "A", "luz_solar": True, "precio": 1500},
    {"especie": "B", "luz_solar": False, "precio": 2000},
    {"especie": "C", "luz_solar": True, "precio": 1000}
]

def agregar_planta(d_plantas, nueva_planta):
    d_plantas.append(nueva_planta)
    print(d_plantas)
    return d_plantas

agregar_planta(a_plantas, {"especie": "D", "luz_solar": True, "precio": 1600})
# """

# ============================================================
"""
3. Se representa un ticket de supermercado como una lista de diccionarios, donde cada diccionario tiene la siguiente información:
● Nombre del producto
● Precio por unidad
● Cantidad
Se pide hacer una función que reciba el ticket y devuelva el monto total a pagar.
"""
# ============================================================

print('Ejercicio 3')
# """
a_tickets = [
    {"nombre_del_producto": "A", "precio_por_unidad": 1000, "cantidad": 1},
    {"nombre_del_producto": "B", "precio_por_unidad": 1000, "cantidad": 6},
    {"nombre_del_producto": "C", "precio_por_unidad": 2000, "cantidad": 7}
]

def monto_total_a_pagar(a_tickets):
    largo_tickets = len(a_tickets)
    precio_total = 0
    for i in range(0, largo_tickets):
        precio_total += a_tickets[i]['precio_por_unidad'] * a_tickets[i]['cantidad']
    print(precio_total)
    return precio_total

monto_total_a_pagar(a_tickets)
# """

# ============================================================
"""
4. Sol tiene una lista de diccionarios donde guarda todas las películas que vió. 
La información que tiene para cada una es: el nombre de la serie, año en que salió, y la puntuación que le puso del 1 al 10. 
Hace mucho que quiere que Tomás empiece a ver las películas que ella considera que son las mejores que vio.
Hacer una función que reciba el diccionario de las películas que vió Sol, y que devuelva una nueva lista de diccionarios donde sólo estén las películas que tienen puntaje mayor a 7.
"""
# ============================================================

print('Ejercicio 4')
# """
a_peliculas = [
    {"nombre": "A", "anio_estreno": 2004, "puntuacion": 10},
    {"nombre": "B", "anio_estreno": 2010, "puntuacion": 6},
    {"nombre": "C", "anio_estreno": 2025, "puntuacion": 7},
]


def puntuacion_mayor_a_siete(a_peliculas):
    largo_peliculas = len(a_peliculas)
    puntuacion_mayor_a_7 = []
    for i in range(0, largo_peliculas):
        if (a_peliculas[i]['puntuacion'] > 7):
            puntuacion_mayor_a_7.append(a_peliculas[i])
    print(puntuacion_mayor_a_7)
    return puntuacion_mayor_a_7


puntuacion_mayor_a_siete(a_peliculas)
# """

# ============================================================
"""
5. Un profesor guarda las notas del primer parcial de sus alumnos en una lista de diccionarios que guarda la siguiente información:
● Nombre
● Apellido
● Intento
● Nota
Donde ”intento” es la instancia que está rindiendo, 1 si es la primera vez que rinde el parcial, 2 si es el primer recuperatorio y 3 si es el segundo recuperatorio. 

Se pide hacer una función que, dado esta lista de diccionarios, devuelva el promedio de las notas en la primera oportunidad que rindieron los alumnos
 
¿Cómo harían para generalizar la función y que el intento sea parametrizable? Es decir, que no solamente sirve para el intento 1, sino que también pueda servir para los demás.
"""
# ============================================================


print('Ejercicio 5')
# """
a_notas = [
    {
        "nombre_estudiante": "A",
        "apellido_estudiante": "A",
        "intento": 1,
        "nota": 10,
    },
    {
        "nombre_estudiante": "B",
        "apellido_estudiante": "B",
        "intento": 2,
        "nota": 6,
    },
    {
        "nombre_estudiante": "C",
        "apellido_estudiante": "C",
        "intento": 3,
        "nota": 7,
    },
    {
        "nombre_estudiante": "C",
        "apellido_estudiante": "C",
        "intento": 1,
        "nota": 5,
    },
]

def promedio_parcial(lista_estudiantes, intento_p):
    largo_lista = len(lista_estudiantes)
    count = 0
    notas = 0
    for i in range(0, largo_lista):
        if(lista_estudiantes[i]['intento'] == intento_p):
            count += 1
            notas += lista_estudiantes[i]['nota'] 
    promedio_del_parcial = notas // count # // 7 - / 7.5
    print(promedio_del_parcial)
    return promedio_del_parcial
promedio_parcial(a_notas, 1)
# """

# ============================================================
"""
6. En una fábrica, se hace un chequeo de calidad a los productos antes de cada entrega. El resultado del chequeo de la entrega se guarda en una lista de  diccionarios, donde cada diccionario tiene la siguiente
información de cada producto:
● Código del producto
● Fecha de vencimiento
● Si pasó el chequeo de calidad o no
Se pide hacer una función que reciba esta lista de diccionarios y elimine todos los productos que no pasaron el chequeo de calidad. 
Devolver en una tupla el diccionario con los elementos eliminados y la cantidad de elementos que quedaron en el diccionario.
Dado que la tupla es inmutable y nosotros no podemos ir agregando elementos a una tupla, ¿En qué momento deberíamos crear la tupla?
"""
# ============================================================

print('Ejercicio 6')
# """
import copy
a_productos = [
    {
        "codigo_del_producto": "A",
        "fecha_de_vencimiento": "A",
        "paso_chequeo": True,
    },
    {
        "codigo_del_producto": "B",
        "fecha_de_vencimiento": "B",
        "paso_chequeo": True,
    },
    {
        "codigo_del_producto": "C",
        "fecha_de_vencimiento": "05/05/25",
        "paso_chequeo": False,
    },
    {
        "codigo_del_producto": "C",
        "fecha_de_vencimiento": "10/10/25",
        "paso_chequeo": False,
    },
]

def chequeo_de_calidad(lista_fabrica):
    largo_lista_original = len(lista_fabrica)
    largo_lista_final = 0
    copia_lista_fabrica = copy.deepcopy(lista_fabrica)
    diccionarios_eliminados = []
    for i in range(0, largo_lista_original):
        if(lista_fabrica[i]['paso_chequeo'] == False):
            # diccionarios_eliminados.append(lista_fabrica[i])
            diccionarios_eliminados.insert(0, copia_lista_fabrica[i])
            # print("* diccionarios_eliminados", diccionarios_eliminados)
            # print("lista_fabrica[i]", lista_fabrica[i])
            lista_fabrica[i].clear()
            # claves = lista_fabrica[i].items()
            # print("claves", claves)
            """
                for j in claves:
                # print("claves[0]", claves[0])
                # print("j", j) # ('codigo_del_producto', 'C') | ('fecha_de_vencimiento', 'C') | ('paso_chequeo', False)
                print("j[0]", j[0]) # codigo_del_producto | fecha_de_vencimiento | paso_chequeo
                print("lista_fabrica[i]", lista_fabrica[i])
                print('lista_fabrica[i][j[0]]', lista_fabrica[i][j[0]])
                # print(lista_fabrica[i][j[0]])
                (lista_fabrica[i]).popitem()
            """
    print("* diccionarios_eliminados", diccionarios_eliminados)
    print("- lista_fabrica", lista_fabrica) # [{'codigo_del_producto': 'A', 'fecha_de_vencimiento': 'A', 'paso_chequeo': True}, {'codigo_del_producto': 'B', 'fecha_de_vencimiento': 'B', 'paso_chequeo': True}, {}, {}]
    tupla_final = (diccionarios_eliminados, largo_lista_original)
    print("tupla_final", tupla_final)

chequeo_de_calidad(a_productos)
# """

# ============================================================
"""
7. Se quiere guardar la información de un grupo de maratonistas. Se necesita guardar su nombre, DNI, y todas las maratones que corrió, de la cual a su vez se quiere tener el nombre de cada una, el año, el puesto en que salió el maratonista, y el tiempo que tardó en terminarla.

a. Crear el diccionario que represente esta situación.
AYUDA: Queremos guardar muchos maratonistas, y a su vez, muchas maratones para cada maratonista, entonces ¿Qué tipo de dato debería ser el campo que guarda todas las maratones? ¿Y qué tipo de dato es la maratón en sí?
b. Teniendo una lista de diccionarios de maratonistas, ordenarlos alfabéticamente.
c. Ordenar las maratones de cada maratonista según el tiempo que tardó en completar cada una de forma ascendente
"""
# ============================================================

print('Ejercicio 7')
# """
maratonistas = [
    {
        "nombre": "V",
        "dni": "12123456",
        "maratones": [
            {
                "nombre_maraton": "XYZ",
                "tiempo_maraton_min": 45,
            },
            {
                "nombre_maraton": "ABC",
                "tiempo_maraton_min": 65,
            },
        ],
    },
    {
        "nombre": "L",
        "dni": "12123456",
        "maratones": [
            {
                "nombre_maraton": "POU",
                "tiempo_maraton_min": 88,
            },
            {
                "nombre_maraton": "QWE",
                "tiempo_maraton_min": 30,
            },
        ],
    },
]

# maratonista es maratonistas[i] = {}
maratonistas_alfabeticamente = sorted(
    maratonistas, key=lambda maratonista: maratonista["nombre"]
)
# print("maratonistas_alfabeticamente", maratonistas_alfabeticamente)

for maratonista in maratonistas_alfabeticamente:
    print("maratonista['maratones'][0]", maratonista['maratones'][0])
    maratonista['maratones'].sort(key=lambda maraton: maraton['tiempo_maraton_min'],)
print("maratonistas_alfabeticamente", maratonistas_alfabeticamente)
# """

"""for i in maratonistas_alfabeticamente:
    print("i['maratones'][0]['tiempo_maraton_min']", i['maratones'][0]['tiempo_maraton_min'])"""