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

numero = 10
while numero <= 30:
    if numero % 3 == 0:
        print("El primer número múltiplo de 3 es:", numero)
    break
numero += 1

# 2.2.2. Continue
"""
La declaración continue se utiliza para saltar una iteración del bucle y continuar con la siguiente iteración. Es
decir, cuando se encuentra una instrucción continue, el programa se salta el resto del bloque de código del
bucle para esa iteración específica y continúa con la siguiente iteración.
"""

numero = 1
while numero <= 10:
    if numero % 2 == 0:
        numero += 1 # Si es par, suma 1 y saltar a la siguiente iteración
    continue
    print(numero)
    numero += 1