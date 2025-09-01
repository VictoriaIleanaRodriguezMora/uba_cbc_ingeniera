# Sesion 2
Estructuras de control:
Estructuras condicionales
- selectivas

Estructuras iterativas

![alt text](image.png)
Por un lado, el continue está de más. Si el bloque dentro del while llega a la última línea, simplemente vuelve
a empezar. No hace falta que le aclaremos con el continue que “tiene que volver a empezar”. El continue es
para cuando nosotros queremos forzar que vuelva a iterar. Por el otro, el if dentro del while con el break
tampoco tiene sentido. Primero, porque con el continue ahí nunca se ejecutaría y además, como dijimos más
numero < 3.
arriba, la condición es que
En el momento en el que numero llega a 3, el while deja de
cumplir con la condición, y la ejecución se corta. Por lo que el if sólo estorba, haciendo algo que ya de por sí
iba a hacer el while.