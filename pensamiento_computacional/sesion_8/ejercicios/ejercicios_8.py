# GUIA DE EJERCICIOS Nº6 – Archivos

# ============================================================
# 1. Se tiene un archivo con la pregunta “¿Cómo estás hoy?” llamado pregunta.txt. Se pide leerlo y mostrar la pregunta por pantalla para luego pedirle al usuario que ingrese una respuesta. Después, guardar la respuesta dada por el usuario en el archivo.
"""
Por ejemplo, se tiene el archivo pregunta.txt que originalmente tiene:
¿Cómo estás hoy?
Y el usuario da la respuesta: “¡Bien, porque me comí una hamburguesa!”
Entonces el archivo debería quedar de la forma:
¿Cómo estás hoy?
¡Bien, porque me comí una hamburguesa!
"""
# Modo r+: Lectura = que 'r', 
# Escritura = empieza a escribir desde el comienzo del archivo. Pisa caracter por caracter del contenido previo.
# Si leo y escribo, empieza a escribir desde el final, porque al leer, el puntero queda en el final-.
# ============================================================

# """
ej_01_file_read = open('pensamiento_computacional/sesion_8/ejercicios/pregunta.txt', 'r+', encoding='utf-8')
lines_ej_01_file_read = ej_01_file_read.readlines() # array donde cada posicion es una linea del archivo
print(lines_ej_01_file_read)

lines_limpio_ej_01 = ''
for lines in lines_ej_01_file_read:
    lines_limpio_ej_01 += (lines.strip('\n')) + ' '

rta_user = input(lines_limpio_ej_01)
print("rta_user", rta_user)

ej_01_file_read.write(rta_user + '\n')
# """

# ============================================================
# 2. En un archivo llamado regalo.txt se tiene la lista de las personas que quieren participar en el regalo de cumpleaños de Sol (en cada línea está el nombre de una persona). El encargado de organizar el regalo es Ale, y quiere saber más información antes de ir a comprarle algo a Sol.
# a. Mostrar por pantalla los nombres de las personas que quieren participar en el regalo.
# b. Se sabe que quieren poner 1000 pesos por persona por regalo. Hacer una función que devuelva cuánto dinero tiene Ale para hacerle el regalo a Sol. Es decir si se tiene un archivo de esta forma:
"""
Agus
Manu
Santi
Lorena
Maria
La función tiene que devolver 5000
"""
# c. Tomi sabe que si participa Santi, también participa Tomi. Se pide que si Santi está en el archivo de los nombres, se agregue también a Tomi.
# ============================================================


# """
ej_02_file_read = open('pensamiento_computacional/sesion_8/ejercicios/regalo.txt', 'r+', encoding='utf-8')
lines_ej_02_file_read = ej_02_file_read.readlines() # array donde cada posicion es una linea del archivo
print(lines_ej_02_file_read) # ['Agus\n', 'Manu\n', 'Santi\n', 'Lorena\n', 'Maria']

monto_total_para_regalo = 0

personas_que_participan_en_el_regalo = []
for lines in lines_ej_02_file_read:
    personas_que_participan_en_el_regalo.append((lines.strip('\n')) + ' ')
    if(lines.count("Santi")): # si lines.count("Santi") > 0
        personas_que_participan_en_el_regalo.append('Tomi')
        ej_02_file_read.write('\n' + 'Tomi' + '\n')

print(personas_que_participan_en_el_regalo)

personas_final = []
print('Personas que participan en el regalo:')
for persona in personas_que_participan_en_el_regalo:
    print(persona)

print(f"Presupuesto total: ${(len(personas_que_participan_en_el_regalo) * 1000)}")
# """

# ============================================================
# 3. En un hogar se quieren organizar mejor con las compras, por lo que se quiere guardar en un archivo la lista de productos que se necesitan para la próxima vez que la familia vaya al supermercado. 
# Se pide hacer un programa que cree un archivo de compras.txt (Ayuda: abrir el archivo en modo w) y le pregunte al usuario qué necesita comprar hasta que ingrese una X. Por ejemplo:
"""
> ¿Qué agrego a la lista de compras?
> Papa
> ¿Qué agrego a la lista de compras?
2
> Pollo
> ¿Qué agrego a la lista de compras?
> Fideos
> ¿Qué agrego a la lista de compras?
> X
El archivo tendría que estar de la siguiente forma:
Papa
Pollo
Fideos
"""
# ============================================================

# """
ej_03_file_append = open('pensamiento_computacional/sesion_8/ejercicios/compras.txt', 'a', encoding='utf-8')
lista_de_compras = [];
item_a_agregar = input('> ¿Qué agrego a la lista de compras? ');
lista_de_compras.append(item_a_agregar + '\n')

while(item_a_agregar != 'X'):
        item_a_agregar = input('*> ¿Qué agrego a la lista de compras? ')
        if(item_a_agregar != 'X'):
            lista_de_compras.append(item_a_agregar + '\n')

ej_03_file_append.writelines(lista_de_compras)
# """

# ============================================================
# 4. Se tiene un archivo con el siguiente texto:
"""
Paco Peco, chico rico,
insultaba como un loco
a su tío Federico;
y éste dijo: Poco a poco,
Paco Peco, poco pico. Me han dicho que has dicho un dicho
que han dicho que he dicho yo,
el que lo ha dicho, mintió,
y en caso que hubiese dicho
ese dicho que tú has dicho
que han dicho que he dicho yo,
dicho y redicho quedó.
y estaría muy bien dicho,
siempre que yo hubiera dicho
ese dicho que tú has dicho
que han dicho que he dicho yo.

Se pide hacer un programa que pida dos palabras: una que se quiera reemplazar y la palabra por la que se quiera reemplazar, cambie el texto y lo guarde en el archivo otra vez. Por ejemplo, si la función recibe “poco” y “mucho”, reemplaza “poco” por “mucho” todas las veces que aparezca en el texto.
"""
# ============================================================


ej_04_read = open('pensamiento_computacional/sesion_8/ejercicios/ej_04.txt', 'r', encoding='utf-8')
string_ej_04 = ej_04_read.read() # Todo el contenido en un string. Tiene los saltos de línea implicitos
# print(string_ej_04)

a_reemplazar = input('Ingrese la palabra que quiere reemplazar ')
reemplazar_por = input('Ingrese la palabra con la que quiere reemplazar por ')

new = string_ej_04.replace(a_reemplazar, reemplazar_por)

ej_04_write = open('pensamiento_computacional/sesion_8/ejercicios/ej_04.txt', 'w', encoding='utf-8')
ej_04_write.write(new)
