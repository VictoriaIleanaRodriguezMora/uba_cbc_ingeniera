# - Tipos de datos

# Se cuenta desde cero

# Numeros
# Función type - Me dice el tipo de dato de la variable
a = 10
print(a) # 10
print(type(a)) # <class 'int'>

a = 'Victoria'
print(a) # Victoria
print(type(a)) # <class 'str'>

a = 20.9
print(a) # 20.9
print(type(a)) # <class 'float'>

x = 10
y = 5.5
z = x + y
print(type(z)) # <class 'float'>

# Las operaciones siempre van a dar un flotante
division = x / y

# Cadenas
nombre = 'Pensamiento'
apellido = 'Computacional'

# Funcion len() - Conocer el largo de un string
largo_nombre = len(nombre) # Captura el largo, la cantidad de caracteres de la variable
print(largo_nombre)

# Concatenar 2 strings
nombre_materia = nombre + ' ' + apellido
print(nombre_materia)

# Cortar un string - [::] Operador substring
# variableAUsar[desde_donde:hasta_donde:cada_cuantas_letras] 
# [start:stop:step] Por defecto es: desde el principio, hasta el final y todas las letras

# nombre_corto = nombre[::] # Así, no genera ningun cambio, lo deja como estaba
# nombre_corto = nombre[5::] # miento. Empieza desde el nro que le digo INCLUIDO
# nombre_corto = nombre[5:8:] # mie. Empieza desde el 5 INCLUIDO, hasta la 8 INCLUIDO
nombre_corto = nombre[5:8:2] # me. Empieza desde el 5 INCLUIDO, hasta la 8 INCLUIDO. SALTANDO cada 2 letras
print(nombre_corto)

# Tipos de datos -

# - Ingreso de datos por el usuario

# Funcion input() - Hace que el programa se quede esperando a que el usuario ingrese un valor
# Acá no es cómo en js que para pedir un dato tengo que ejecutarlo en el navegador, lo ingreso por la terminal

# valor = input("Ingrese un valor:") # input() - No aparece ningún mensaje sobre qué ingresar
# print(valor) # 8 
# print(type(valor)) # <class 'str'>

5 != '5' != 5.0 # Todos son 5 en distintos tipos de datos

""""
numero = input("Ingrese un nro") # 10
numero2 = input("Ingrese otro nro") # 5
suma = numero + numero2
print(suma) # 105 ---> concatena los strings ingresados
"""

# Parsear
"""

numero = int(input("Ingrese un nro: ")) # 10
numero2 = int(input("Ingrese otro nro: ")) # 5
suma = numero + numero2
# Si uso float en vez de int, devuelve 15.0
print(suma) # 15 ---> suma ✅
"""

# Ingreso de datos por el usuario - 

# - Funciones

# Funciones -
# Buena practica. Documentar que recibe la fn, que hace, fin, porque se creo. Condicion que debe cumplir los parametros para que funcione
def saludar(nombre):
    print("Holaa! " + nombre)
saludar("Victoria")
saludar("Ileana")

# el llamado a la funcion saludar y la definicion de saludar, estan ambos en el scope global. en la identacion 0

# Devuelve la suma de 2 numeros
"""
def suma(sumando1, sumando2):
    rtado = sumando1 + sumando2
    return rtado
suma(5, 9) # Se ejecuta, pero no veo el resultado. Debo capturar el retorno en una variable

resultado_suma = suma(5, 9)
print(resultado_suma)
"""

def suma_resta(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    return suma, resta

# suma, resta =  suma_resta(10, 9) # Esta manera NO está mal, es posible de usar. Porque estas suma y resta viven en un ambito distinto a las de la funcion. La de la funcion nacio y murió en la funcion. 
a, b =  suma_resta(10, 9) # 'a' es el primer valor que retorna la funcion y 'b' el 2do valor. Confunde, asique es mejor diferenciarlas de alguna manera

print(a, b)

