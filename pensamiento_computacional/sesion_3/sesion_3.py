# Operadores
"""
and or 
not: Operador de negacion. Niega el valor de la variable. Es el !
"""

# Estructuras condicionales
# si pasa tal cosa, entonces, hago tal cosa
"""
si pasa tal cosa
    hago tal cosa
"""

# ‼️ENTONCES ES ':', no hay llaves
"""
if expresion:
    accion_1
"""
# ‼️true va con mayusculas True
"""
hay_sol = False
if hay_sol:
    print("Hay sol!")
else:
    print("No hay sol! Es de noche")
"""
hay_sol = True
hace_frio = True

if hay_sol and (not hace_frio):
    print("Hay sol y no hace frío!")
elif hay_sol and hace_frio:
    print("Hay sol y hace frío!")
elif (not hay_sol) and (not hace_frio):
    print("No hay sol y no hace frío!")
else: #default
    print("No hay sol! Es de noche")

# Definir una función
def division(dividendo, divisor):
    if divisor == 0: # los : significa entonces
        return "No se puede dividir por cero"
    else: 
        resultado = dividendo / divisor
        return resultado

# Esta opcion es igual a la de arriba, cumple mas buenas practicas esta
def division(dividendo, divisor):
    if divisor == 0: # los : significa entonces
        return "No se puede dividir por cero"

    resultado = dividendo / divisor
    return resultado

# Estructuras iterativa
#❗ Esto es un bucle infinito
"""
while (paso<10):
    print(paso)
"""

# Cuando escribo un bucle while, tengo que hacer, dentro del while, dentro de las acciones, tengo que especificar que la condiciones debe cambiar.
# paso < 10, no cambia NUNCA, por eso es un bucle infinito. Esto es siempre verdadero, se ejecuta siempre
# 10 < 10 es FALSE, cuando el bucle da FALSE, SALE del bucle. Termina de ejecutar el bcle
"""
print("Antes del while")
paso = 0;
while (paso < 10): 
    print(paso)
    paso = paso + 1
print("Despues del while")
"""

# Bucle for. Video 14:50
conjunto = [1, 2, 3, 4, 5, 6, 7, 8]
for numero in conjunto:
    print(numero)

# start - stop
conjuntob = ["a", "z", 1 ] # SE PUEDEN MEZCLAR TIPOS DE DATO
for numero in range(1, 11): #incluye el 1er parametro, pero no el 2do
    print(numero)

# start
for numero in range(11): # si no especifico el 'start', arranca desde 0, pero no incluye el 11
    print(numero) 

# start - stop - step
# desde el (start, , ) hasta el (,stop,) en intervalos de (, , step)
for numero in range(6, 11, 2): # si no especifico el 'start', arranca desde 0, pero no incluye el 11
    print(numero) 

