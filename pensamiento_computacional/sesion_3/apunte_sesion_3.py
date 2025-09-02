# Este código se puede mejorar, no es optimo
# Contemos cuántos múltiplos de 3 ingresan en un lote de 5 números
"""
print('Ingresá 5 números enteros');
total_mult = 0
num = int(input('Número: '));
if num % 3 == 0: #identifico si es múltiplo de 3
 total_mult+=1
num = int(input('Número: '));
if num % 3 == 0:
 total_mult+=1
num = int(input('Número: '));
if num % 3 == 0:
 total_mult+=1
num = int(input('Número: '));
if num % 3 == 0:
 total_mult+=1
num = int(input('Número: '));
if num % 3 == 0:
 total_mult+=1
print('Vinieron:',total_mult,'múltiplos de 3')
"""

# ✅ Código mejorado con while
"""
total_multiplos = 0;
condicion_de_corte = 0;
while condicion_de_corte < 5:
    num = int(input('Ingresá 5 números enteros: '));
    if num % 3 == 0:
        total_multiplos += 1
    condicion_de_corte += 1

print("Total números múltiplos de 3 ingresados: ", total_multiplos)
"""


# Imprime saludo por pantalla hasta que usuario ingresa X
"""
print('Te saludo hasta que me dejes')
respuesta = 'S'
while respuesta != 'X':
    print('¡Hola!')
    respuesta = input('¿Querés otro saludo? Ingresá X si la respuesta es no: ')
"""



# 2.2.1. Break
"""
La declaración break se utiliza para salir inmediatamente de un bucle antes de que se complete su iteración
normal. Cuando se encuentra una instrucción break, el programa salta fuera del bucle y continúa con la
ejecución de las instrucciones que están después del mismo.
Ejemplo:
"""

""" ✅ Sin el break, este bucle funciona
numero = 10
print("Antes del bucle")
while numero < 30:
   # print(numero)
    if numero % 3 == 0:
        print("El primer número múltiplo de 3 es:", numero)
        break
    numero += 1
# numero += 1, con esta linea en MAL indentación bucle infinito
print("Despues del bucle")
"""

# 2.2.2. Continue
"""
La declaración continue se utiliza para saltar una iteración del bucle y continuar con la siguiente iteración. Es
decir, cuando se encuentra una instrucción continue, el programa se salta el resto del bloque de código del
bucle para esa iteración específica y continúa con la siguiente iteración.
"""

# """
numero = 1
veces = 0
while numero <= 10:
    if numero % 2 == 0:
        print("if, ANTES",numero)
        numero += 1 # Si es par, suma 1 y saltar a la siguiente iteración
        print("if, DSPS",numero)
        
        continue
        #print("if",numero) # no hace nada
    print(numero)
    numero += 1
    veces += 1
print("despues del bucle: ", numero)
print("despues del bucle veces: ", veces)
# """ 1 2 3 4 5 6 7 8 9 10
"""
1 2 3 4 5 6 7 8 9 10
numero = 1
veces = 0
    if 1 % 2 == 0: # --> falso
        print("if",numero) # --> NO entra aca
        continue # --> NO entra aca
    print(numero)
numero += 1 # --> 2 
veces += 1 # --> 1

--------------------------
    if 2 % 2 == 0: # --> true
        print("if",numero) # --> SI entra aca
        continue
    print(numero)
numero += 1 # --> 2 
veces += 1 # --> 1
"""
    
    
    
"""
Notemos que tanto para el uso de break como de continue, si el código se encuentra con uno de ellos, no
ejecuta nada posterior y vuelve a comenzar el ciclo, evaluando la condición (en el caso del while) y volviendo
a ejecutar el bloque dentro del bucle. Por lo que en ambos ejemplos no tuvimos necesidad de usar un ‘else’:
simplemente al usar el break o el continue sabemos que no se va a ejecutar el código que sigue. Y, si no se
cumple la condición del if, entonces ejecuta el código debajo del bloque y listo.
"""
"""

a = range(2, 4//2+1);
print(a)
num = int(input('Ingresá un número entero positivo: '))
while num <= 0:
    num = int(input('Ingresá un número entero positivo: '))
    cant_divisores = 0
    for d in range(2, num//2+1):
        if num % d == 0:
            cant_divisores += 1
            print(num,'tiene',cant_divisores,'divisores')
"""
         




