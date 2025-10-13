# Sesion 08
Hasta ahora sabemos cómo crear programas que trabajen con variables, estructuras. Pero esa información no persiste en el tiempo, no sólo eso, sino que hoy es complicado trabajar con mucha información. Con información que yo tenga en planillas, en formato .txt o .csv

# Cómo leer archivos y trabajar con esa info
# Pasos
- Abrir el archivo
- Trabajar, manipular el archivo
- Cerrar el archivo

# Pregunta abierta en StackOverflow
[Python doesn't find my file but it is in the same directory]([cont](https://stackoverflow.com/questions/79778354/python-doesnt-find-my-file-but-it-is-in-the-same-directory))

### La ruta relativa es 'Desktop/VICKY/VICKY_TAREAS/UBA/uba_cbc_ingenieria'
La ruta de la que la funcion open parte, es 'Desktop/VICKY/VICKY_TAREAS/UBA/uba_cbc_ingenieria'. Por eso debo especificar la ruta del archivo, a partir de esta.
![La ruta de la que la funcion open parte, es 'Desktop/VICKY/VICKY_TAREAS/UBA/uba_cbc_ingenieria'](/video/img/image.png)
![Estructura de carpetas](/video/img/image-1.png)

# /n
- El caracter /n es, genera un salto de línea. Es un caracter no visible. Cómo %20

En el archivo de texto, no tengo escrito /n. Lo que pasa es que al leer, guardar y mostrar el contenido de cancion.txt. Ese salto de línea que yo tengo en el archivo, se representa, se agrega cómo /n. Por eso tengo /n al final de cada posición del arreglo, porque cada posición es una línea del archivo, y cada línea del archivo tiene un salto de línea.

Me confunde que se cierre y despues lo manipulo

# Archivos CSV. Comma Separated Value



# argumento y parametro
- https://learn.microsoft.com/es-es/dotnet/visual-basic/programming-guide/language-features/procedures/differences-between-parameters-and-arguments
- [¿Cual seria la diferencia entre parámetros y argumentos de una función?](https://es.stackoverflow.com/questions/62004/cual-seria-la-diferencia-entre-par%C3%A1metros-y-argumentos-de-una-funci%C3%B3n)
Un parámetro representa un valor que el procedimiento espera que tú pases cuando lo llames. La declaración del procedimiento define sus parámetros.
Un argumento representa el valor que se pasa a un parámetro de procedimiento al llamar al procedimiento. El código de llamada proporciona los argumentos cuando llama al procedimiento.

# El programa es independiente de los datos
Si los datos cambian, no cambia el programa. Si diseño un programa, para un formato especifico de datos, y ese archivo cambia, el programa no se ve modificado. Mismo si cambia un dato. 
