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




# 6. 