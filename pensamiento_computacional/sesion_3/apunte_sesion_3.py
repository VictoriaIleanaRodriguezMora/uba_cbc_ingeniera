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
# Consigna: Contemos cuántos múltiplos de 3 ingresan en un lote de 5 números
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

"""
numero = 1
veces = 0
while numero <= 10: # en la última vuelta, entra valiendo 10, y sin continue suma 2 veces, por eso sale valiendo 12
    if numero % 2 == 0: # cuando numero es par entra.
        print("if, ANTES",numero)
        numero += 1 # Si es par, suma 1 y saltar a la siguiente iteración
        continue
        print("if, DSPS",numero)
    # si el nro no es par, pasa por acá
    print(numero)
    numero += 1
    veces += 1
print("despues del bucle: ", numero)
print("despues del bucle veces: ", veces)
""" 
   
    
"""
Notemos que tanto para el uso de break como de continue, si el código se encuentra con uno de ellos, no
ejecuta nada posterior y vuelve a comenzar el ciclo, evaluando la condición (en el caso del while) y volviendo
a ejecutar el bloque dentro del bucle. Por lo que en ambos ejemplos no tuvimos necesidad de usar un ‘else’:
simplemente al usar el break o el continue sabemos que no se va a ejecutar el código que sigue. Y, si no se
cumple la condición del if, entonces ejecuta el código debajo del bloque y listo.
"""


# 3. Rangos
rango_a = range(1,10)
# print(rango_a) # range(1, 10)
# No se puede ver al valor de los rangos si no se los recorre! 
range(1,10) # 1,2,3,4,5,6,7,8,9
range(6) # 0,1,2,3,4,5
range(0,8,2) # 0,2,4,6

# no entiendo esto
range(15,10,-5) # 15
range(15,10,-1) # 15, 14, 13, 12, 11

# ✅ Código con rangos y for
# Consigna: Contemos cuántos múltiplos de 3 ingresan en un lote de 5 números
"""
total_multiplos = 0;
condicion_de_corte = 0;
range_c = range(1, 6)
for range_item in range_c:
    num = int(input('Ingresá 5 números enteros: '));
    if num % 3 == 0:
        total_multiplos += 1
print("Total números múltiplos de 3 ingresados: ", total_multiplos)

"""

# 4. Bucles anidados
# Calcular los divisores de un nro
# Condiciones: * El nro a evaluar, no puede ser cero. Cero no tiene divisores
""" 
num_user = int(input("Ingresa un numero natural mayor a cero: "))
while(num_user > 0):
    cantidad_de_divisores = 0;
    mitad_de_num_user = num_user // 2;
    # El rango, no incluye el final. Osea, yo ingreso 8 // 2, y eso da 4. Pero al recorrer no está llegando a 4, porque range no lo incluye. Tengo que sumarle 1
    rango_de_nros_a_evaluar = range(2, mitad_de_num_user + 1)
    for num in rango_de_nros_a_evaluar:
        print(f"****num {num}")
        if num_user % num == 0:
            cantidad_de_divisores += 1
            print(f"{num_user} % {num}: {num_user % num}")
            print("cantidad_de_divisores += 1: ", cantidad_de_divisores)
    print(f"Total divisores de {num_user}: {cantidad_de_divisores}. Sin incluir a sí mismo y a 1.")
    num_user = int(input("Ingresa un numero natural mayor a cero: "))
print(f"Ingresaste un número menor a cero: {num_user}. Saliste del bucle")
"""
