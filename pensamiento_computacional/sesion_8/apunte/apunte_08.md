1ro me estaba equivocando en esto: 
```py
completo = open('pensamiento_computacional/sesion_8/apunte/datosCompletos.csv', 'w') # Crea el archivo datosCompletos
```
no estaba poniendo `datosCompletos.csv`, estaba poniendo `comma_separated_value.py`

     
Después, me estaba equivocando en que en el código estaba haciendo: `a[i] = a[i].split(';') # Arma tabla quitando ;`, estaba spliteando en **`;`** y mis csv estaban escritos con **`,`**, por eso me daba error

# Funciones lambda - Funciones anónimas
# Return en lambda
No tienen return explicito. Están pensadas y diseñadas para ser funciones pequeñas, simples, que solo tienen una expresión. 
El return es cómo las funcion flecha de js, está implicito.

# Funcione de orden superior
Pueden aceptar funciones como argumentos, devolver funciones cómo resultados y almacenar fn en variables

# Sin lambda
```py
def retornar_nota(estudiante):
    return estudiante[1]

lista_estudiantes = [('Edward', 4.2),
                     ('Pepe', 2.5),
                     ('Maria', 3.1),
                     ('Carlos', 4.5)]

lista_ordenada = sorted(lista_estudiantes, key=retornar_nota, reverse=True)
print(lista_ordenada)
```

# Con lambda
```py
lista_estudiantes = [('Edward', 4.2),
                     ('Pepe', 2.5),
                     ('Maria', 3.1),
                     ('Carlos', 4.5)]
# Es cómo si se ejecutara en base a la lista.
lista_ordenada = sorted(lista_estudiantes, key = lambda arg_que_acepto : arg_que_acepto[1] , reverse=True)
print(lista_ordenada)
```
