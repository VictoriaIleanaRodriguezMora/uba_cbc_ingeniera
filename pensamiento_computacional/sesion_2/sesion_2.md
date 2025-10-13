# Sesion 2
### Lenguajes fuertemente tipados: 
Cuando defino/declaro una variable y el tipo de dato con el que se crea es con el que se va a mantener durante toda la ejecución del programa. Una variable desde que nace hasta que muere tiene un sólo tipo de dato, que yo defino. 

Hay otros lenguajes cómo python, que no son fuertemente tipados. Osea que el tipo de dato de la variable se infiere desde el valor que yo le doy cuando la creo. 
 
Algunos son debilmente tipados.

x = 10
x = 'fhgd'
esto no se puede n lenguajes fuertemente tipados

La ejecución del código es scuencial

Tipos de datos: int, str, float

Enteros: Se pueden sumar, restar, multiplicar, dividir
No siempre va a dar entero operar numeros, la mayoría de las veces da con coma. Y aunque sea un entero, da .0

Con el operador + sumo numeros y concateno strings

Se cuenta desde cero

- Funciones. Son bloques de código que permiten modularizar el programa
- Modularizar: Cuando los programas son grandes o largos, se resuelven varias cosas al mismo tiempo. Se crean funciones para resolver objetivos especificos
def, viene de define
def nombreFuncion(): ----> Firma de una funcion

Si quiero que el bloque dentro de la funcion se ejecute debo llamarlo, invocarlo. Si no lo hago, la funcion por si sola no hace nada. 

Puedo llamar a una función las veces que quiera

Identacion

Los parametros me permiten tener funciones dinamicas
def nombreFuncion(parametro):

Ambitos, scopes
Cada funcion define su propio ambito

Está el global, de todo el archivo y el local dentro de la funcion
Los ambitos se definen por la identeacion

La mayoria de las veces queremos que la función nos devuelva un valor, para usar en otro lado

Las funciones permiten recibir muchos valores, pero tambien devolver muchos valores

![alt text](/img/image.png)
https://medium.com/@rishu__2701/this-article-will-teach-you-about-operator-precedence-and-associativity-in-python-ee455c7fbfee
