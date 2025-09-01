# 2.2.1. Manipulando Strings

# los caracteres comienzan en la posición 0,
palabra = "pensamiento"
print(palabra[1:3]) # en
print(palabra[3:7]) # sami
# Si no aclaro inicio, se considera que comienza desde el cero
print(palabra[:3]) # pen
# Si no aclaro final, finaliza en el extremo derecho de la palabra
print(palabra[3:]) # samiento

print(palabra[:10:2]) # pnain | es lo mismo [0:10:2]

# asume que desde el principio, hasta el final
print(palabra[::3]) # psit


# 2.3. Input y casteos

# casteo de entero
print(int('3')) # --> 3 int
print(int(2.8)) # --> 2
print(int(1)) # --> 1

# casteo a str
print(int(1)) # --> '1'
print(int(2.8)) # --> '2.8'
print(int(1)) # --> 1

# casteo a float
print(int(1)) # --> 1.0

# edad = input('Ingrese la edad de Juan: ') # mensaje al pedir un dato
# print('La edad de Juan es', edad)


dia_semana = "Miércoles"
dia_mes = 8
# Son todas formas iguales de imprimir lo mismo
# Usando +:
print("El día de la semana es: " + dia_semana)
print("El día del mes es: " + str(dia_mes))
# Usando comas:
print("El día de la semana es: ", dia_semana)
print("El día del mes es: ", str(dia_mes))
# Usando f""
print(f"El día de la semana es: {dia_semana}")
print(f"El día del mes es: {str(dia_mes)}")

""""
Ejercitación
Vamos a calcular la edad de un hermano mayor.
Pediremos nombre y edad de una persona, luego cuántos años más tiene su hermano y su nombre e
informaremos la edad del hermano.
Debemos pedir el nombre de las dos personas. Debemos pedir la diferencia de edad. ¿Tendremos que pedir
las dos edades? En realidad, sólo una, la otra podemos calcularla. Luego decidimos qué datos presentar como
salida de ¡nuestro maravilloso programa!
Nuestro programa:
"""
"""
nombre_1 = input("Hola! Decime tu nombre :)");
edad_1 = int(input("Hola! Decime tu edad :)"));

nombre_hermano = input("Cual es el nombre de tu hno? :)");
edad_hermano = int(input("Cuantos años más que vos tiene tu hno? :)"));

print(f"El hermano menor tiene {edad_1} y el mayor {edad_1 + edad_hermano}  ")
"""



# Funciones
"""
Ejemplo return:
"""
nombre = "Logan"
def obtener_saludo(nombre):
    return "Hola, " + nombre
saludo = obtener_saludo(nombre) # -> Esto es lo importante, antes no se asignaba ningúnvalor, ahora que retorna algo, sí
# !!!! Si no hacés nada más, no vas a ver nada en pantalla. Entonces lo printeamos para ver que esté todo ok:
print(saludo)




