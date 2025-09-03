# Ejercicios sesión 3


# Expresiones
# 1. ✅ Escribir la expresión para saber si un número es más grande que otro. Guardarla en una variable de tipo bool e imprimirla por pantalla para ver su valor.
""" 
nro_a = 0
nro_b = 1
nro_a_mayor_nro_b = nro_a > nro_b
print(f"Nro a: {nro_a} es mayor a nro b {nro_b} ? {nro_a_mayor_nro_b} ")
""" 

# 2. ✅ Repetir el punto anterior pero con la expresión que determina que una letra NO es vocal.
""" 
letra = "v"
if((letra != "a") or (letra != "e") or (letra != "i") or (letra != "o") or (letra != "u"))  :
    print(f"{letra} no es una vocal")
""" 


# 3. ✅ Repetir pero para la expresión que permite saber si un número es par y menor a 10.
""" 
if (nro_a % 2 == 0) and  (nro_a < 10):
    print(f"{nro_a} es par y menor a 10")
""" 

# Estructuras de control condicionales
# ✅ 4.Crear una función que dado un número, devuelva su valor absoluto.
""" 
def valor_absoluto(num):
    return abs(num)

val_abs_mi_num = valor_absoluto(-33)
print(f"Mi valor absoluto es: ", val_abs_mi_num)
""" 

# 5. ✅Crear el programa al que sea imposible ganarle en el juego de “Piedra, papel o tijera”. 
""" 
Cada elemento va a ser representado con una letra: 
R para piedra, P para papel y T para tijera.
a. Hacer una función que le haga al usuario ingresar alguna de esas letras, e imprima por pantalla la jugada para ganarle. Por ejemplo:
> ¡Juguemos! Ingresá piedra ( R), papel (P) o tijera (T)
> P
> Tijera. ¡Te gané!
ATENCIÓN: Observar cómo se usa una frase inicial para darle a entender al usuario lo que tiene que hacer (en este caso ingresar alguna de las tres letras).
b. Mostrar por pantalla el mensaje “NO vale” cuando el usuario ingresa una letra no válida (distinta de R, P o T).
""" 

""" 
def piedra_papel_tijera ():
    user_choose = input("> ¡Juguemos! Ingresá piedra (R), papel (P) o tijera (T) ")
    if(user_choose != "r" or user_choose != "p" or user_choose != "t"):
        user_choose = input("Esa letra no vale, ingresá otra: ")
        
    if(user_choose == "r"): # Elige piedra
        print("Papel. ¡Te gané!")
        return "Papel. ¡Te gané!"
    elif(user_choose == "p"): # Elige papel
            print("Tijera. ¡Te gané!")
            return "Tijera. ¡Te gané!"
    elif(user_choose == "t"): # Elige tijera
            print("Piedra. ¡Te gané!")
            return "Piedra. ¡Te gané!"

val_user = piedra_papel_tijera()
print(f"Resultado de piedra, papel o tijera: ", val_user) # esto da none, pq la funcion no devuelve nada sin un return
""" 




# 6. ✅cEscribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con ese valor. Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”.
# Extra: ¿Cómo harían para que el programa quede generalizado para cualquier límite, a elección del usuario, y no solo para 100?.

"""
def determinar_sumar(num_a, num_b, limite):
    if ((num_a + num_b) < limite ):
        print(f"A {num_a} + {num_b} = {num_a + num_b}. Le faltan {limite - (num_a + num_b)} para llegar a {limite}")
    else:
        print(f"La suma da igual que el límite")

determinar_sumar(5, 5, 10)
determinar_sumar(5, 5, 100)
"""

# 7. ✅ Se tienen letras para representar las estaciones del año:
"""
● V para verano
● O para otoño
● I para invierno 
● P para primavera
Crear una función que dada una letra, imprima por pantalla la estación del año que representa (es decir, si se ingresa V se mostrará por pantalla el mensaje “Verano”). En caso de no representar a ninguna estación mostrar un mensaje que diga “error”. Probar la función creada llamándola con A, P, O, B, V e I.
"""

"""
def estaciones_anio(letra):
    if(letra == "V"):
        print("Verano")
    elif(letra == "O"):
        print("Otoño")
    elif(letra == "I"):
        print("Invierno")
    elif(letra == "P"):
        print("Primavera")
    else:
        print("Error")

estaciones_anio("A")
estaciones_anio("P")
estaciones_anio("O")
estaciones_anio("B")
estaciones_anio("V")
"""

# Estructuras de control iterativas

# 8. Se quiere hacer un programa para enseñar a unos niños a contar. Crear una función que reciba un número entero e imprima por pantalla los números del 1 hasta ese número con la estructura de control iterativa for.
"""
def aprender_sumar(nro):
    rango_nros = range(1, nro + 1)
    for num in rango_nros:
        print(f"Número: {num}")

aprender_sumar(17)
"""

# 9. Se quiere mejorar el programa para enseñar matemáticas pensado en el ejercicio anterior. Ahora se necesita una funcionalidad que permita a los niños aprender las tablas. Crear una función que reciba un número entero e imprima por pantalla la tabla de ese número del 1 al 10.
"""
def aprender_tablas(nro):
    rango_nros = range(1, 11)
    for num in rango_nros:
        print(f"Tabla del {nro} --> {nro} * {num}: {num * nro}")

aprender_tablas(2)
"""


# 10. Crear una función que simule un cumpleaños: que dado un entero imprima “Que los cumplas feliz” esa cantidad de veces.
"""
def saludar_cumpleanios(nro_entero):
    rango_a_saludar = range(1, nro_entero + 1)
    for num in rango_a_saludar:
        print(f"Que los cumplas feliz {num}")

saludar_cumpleanios(5)
"""

# 11. ✅ En un almacén están buscando la forma de hacer los cobros más automáticamente. Para esto, se nos pide crear una función que reciba un número entero que representa lo que hay que cobrar, le pida al usuario ingresar un monto, y se vaya mostrando por pantalla cuánto falta para completar el pago. Repetir este proceso hasta que la deuda sea 0 o menor. Por ejemplo, si se recibe el monto 30:
"""
> El importe a pagar es de 30 pesos. Por favor, ingrese un monto.
> 10
> El importe a pagar es de 20 pesos. Por favor, ingrese un monto.
> 15
> El importe a pagar es de 5 pesos. Por favor, ingrese un monto.
> 5
"""
"""

def ejercicio_11():
    monto_total = int(input("Cuanto debe pagar? "))
    monto_pagado = int(input("Ingresé el monto que desea pagar "))
    cuanto_debe = monto_total - monto_pagado
    while(monto_total > monto_pagado):
        print(f"Usd debe {cuanto_debe}. ")
        monto_pagado += int(input("Porfavor, ingrese el monto faltante "))
        cuanto_debe = monto_total - monto_pagado
    print("Usd ya pagó todo lo que debía ")

ejercicio_11() 
"""

# Estructuras de control condicionales e iterativas

# 12. ✅ Escribir código que recorra los números del 1 al 20 y determine para cada uno si es par o impar, imprimiendo un mensaje por pantalla en cada caso.

"""

rango_a_20 = range(1, 21);
for num in rango_a_20:
    if (num % 2 == 0):
        print(f"El número {num} es PAR ");
    else:
        print(f"El número {num} es IMPAR ")
"""
        

# 13. ✅ Se tiene una máquina de sacar juguetes que funciona cuando se ingresa una determinada cantidad de fichas, y se quiere hacer una función que imite ese comportamiento. 3
# a. Hacer una función que reciba un número que represente el precio de la máquina, e imprima por pantalla “Ingresá x fichas para comenzar” hasta que se hayan ingresado esa cantidad de letras F (que representan una ficha), y luego “¡A jugar!” cuando se hayan ingresado todas las fichas necesarias. Por ejemplo, si la función recibe 3, debería tener el siguiente comportamiento:
"""
> Ingresá 3 fichas para comenzar
> F
> Ingresá 3 fichas para comenzar
> F
> Ingresá 3 fichas para comenzar
> B
> Ingresá 3 fichas para comenzar
> F
> ¡A jugar!
"""
"""
def ejercicio_13(cant_fichas_a_cumplir):
    # user_fichas_ingresadas = (input(f"Ingresá {cant_fichas_a_cumplir} fichas para comenzar "))
    contador_fichas = 0
    while(cant_fichas_a_cumplir > contador_fichas):
        user_fichas_ingresadas = (input(f"Ingresá {cant_fichas_a_cumplir - contador_fichas} fichas restantes para continuar "))
        if user_fichas_ingresadas == "f":
            contador_fichas = contador_fichas + 1
            print(f"cant_fichas_a_cumplir {cant_fichas_a_cumplir} - contador_fichas {contador_fichas} ")
            print(f"IF {contador_fichas} ")

ejercicio_13(3)
"""

