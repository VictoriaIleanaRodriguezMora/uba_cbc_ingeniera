> [!NOTE] No reconocen numeros negativos 🔽

```py
isnumeric()
isdecimal()
isdigit()
```

| **Excepción**        | **Causa del error**                                                                                                        |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `AssertionError`     | Falla `assert`.                                                                                                            |
| `AttributeError`     | Falla la referencia de atributos.                                                                                          |
| `EOFError`           | Se genera cuando la función `input()` alcanza la condición de fin de archivo (EOF).                                        |
| `FloatingPointError` | Falla una operación de punto flotante.                                                                                     |
| `GeneratorExit`      | Se genera cuando se llama al método `close()` de un generador.                                                             |
| `ImportError`        | Se genera cuando no se encuentra el módulo importado.                                                                      |
| `IndexError`         | Se genera cuando el índice de una secuencia está fuera de rango.                                                           |
| `KeyError`           | Se genera cuando una key no se encuentra en un diccionario.                                                                |
| `KeyboardInterrupt`  | Se genera cuando el usuario presiona la tecla de interrupción (`Ctrl+C` o Eliminar).                                       |
| `MemoryError`        | Se genera cuando una operación se queda sin memoria.                                                                       |
| `NameError`          | Se genera cuando una variable no se encuentra en el ámbito local o global.                                                 |
| `OSError`            | Se genera cuando la operación del sistema causa un error relacionado con el sistema.                                       |
| `ReferenceError`     | Se genera cuando se utiliza un proxy de referencia débil para acceder a un atributo del referente recolectado como basura. |

# 1.1.1 try except

```py
try:
# Corre este código, algo puede fallar.
except:
# Se ejecuta este código cuando ocurre una excepción en el bloque
de try


try:
# Corre este código, algo puede fallar.
except Excepción_1, Excepción_2:
# Se ejecuta este código cuando ocurre cualquiera de las dos excepciones.


try:
# Corre este código, algo puede fallar.
except Excepción_1:
# Se ejecuta este código cuando ocurre Excepcion_1.
except Excepción_2:
# Se ejecuta este código cuando ocurre Excepcion_2.
```

> [!WARNING] ¡Atención!
> También podríamos querer “no hacer nada” frente a una excepción, pero evitando que el programa se bloquee. Para ello, existe pass.
                  
```py
try:
# Corre este código, algo puede fallar.
except:
pass # No hagas nada.
```

> [!NOTE] pass puede parecer poco útil en un primer momento, pero puede volverse tu mejor amigo. 
> Por ejemplo mientras estás pensando la estructura del código, y querés ir probando algunas líneas cuando aún no está terminado, y evitar que el programa se interrumpa.
> 
```py
if numero % 15 == 0:
    pass
    # Completar.
elif numero % 3 == 0:
    pass
    # Completar.
elif numero % 5 == 0:
    pass
    # Completar.
else:
    pass
    # Completar.
```


> [!WARNING] ¡Atención!
> Los errores deben escribirse exactamente como los identifica Python. En el ejemplo, el Código de error que pretendemos capturar es: ValueError. Debe anotarse tal cual.


# 1.1.1 Cláusula try con else

> [!NOTE] ¿No podemos simplemente poner más código en el bloque try? 
Sí, podemos, pero aquí hay un par de razones por las que esto puede ser una muy mala idea:

> [!CAUTION] 1. Es posible que nos encontremos con excepciones que no anticipamos anteriormente: 
> cuanto más código se encuentre en la cláusula try, más probable será que esto suceda.

> [!CAUTION] 2. Reduce la legibilidad: la cláusula try expresa lo que esperamos que falle, y la cláusula except, las formas en que planeamos manejar las fallas específicas en el código. 
> Cuanto más código se encuentra en la cláusula try, menos claro es lo que realmente estamos intentando, y eso puede hacer que toda la estructura sea más difícil de entender.
> 
Es por esto que el código en el bloque try debe ser lo más pequeño posible, abarcando únicamente a
las líneas de código que podrían resultar en un problema (en un error a atajar).


# 1.1.3. Cláusula try con finally

```py
try:
# Corre este código, algo puede fallar.
except:
# Se ejecuta este código cuando ocurre una excepción en el bloque de try.
else:
# Se ejecuta este código cuando no existe una excepción.
finally:
# Siempre se ejecuta y bloquea el código.
```

> [!TIP] La cláusula finally, es muy especial, ya que:
> - Siempre se ejecutará.
> - Finaliza el programa.
> - Si se produce una excepción no controlada, no importa, ya que finally ejecutará su código antes de que eso ocurra.

> Si tenemos un return en el bloque try, finally interrumpe ese retorno para ejecutar su propio código primero, como se puede observar en el siguiente ejemplo:

```py
def probar_finally():
    try:
        return 2
    finally:
        print("Código del bloque finally")
probar_finally()
# Output:
# Código del bloque finally
# 2
```
> [!TIP] Esta propiedad es extremadamente útil para cualquier situación en la que se requiera una limpieza vital
>
> Después de una operación, como por ejemplo, cuando se trabaja con archivos. 
> 
> Si encontramos algún problema mientras procesamos los datos de un archivo y aún así queremos cerrarlo al terminar, finally nos asegura que esto suceda. 
> 
> Si bien, finally es muy utilizado en código más avanzado, sigue siendo una herramienta importante que debemos conocer en esta etapa.

# 1.1.4. Cláusula raise
En Python, raise nos permite lanzar una excepción si se produce una cierta condición. 

La declaración raise es útil en situaciones en las que necesitamos generar una excepción personalizada como al recibir datos incorrectos o cualquier error de validación.

> [!WARNING] No es correcto lanzar una excepción para atajarla inmediatamente con un except. 
> Lanzar una excepción se suele utilizar para “elevar” el error a una función previa y manejar el error desde ahí. 
> 
> Hay que usar raise de forma razonable.

## 1.1.5 Ejemplo

```py
def calcular_division(x, y):
    try:
        cociente = x / y
    except ZeroDivisionError:
        print(“No se puede dividir por cero.”)
    else:
        print(“El cociente es: “, cociente)
    finally:
        print(“El bloque finally siempre se ejecuta”)
```
### Caso 1: `x = 15`, `y = 5`
```py
calcular_division(15, 5)
# Output
# El cociente es: 5.0 El bloque finally siempre se ejecuta
```

### Caso 1: `x = 15`, `y = 0`
```py
calcular_division(15, 0)
# Output
# No se puede dividir por cero.
# El cociente es: 5.0 El bloque finally siempre se ejecuta
```

> [!NOTE]  Al mismo tiempo, no todas de nuestras validaciones requieren de un try-except: 
> hay validaciones que se pueden hacer tranquilamente con las herramientas de control que ya conocemos: if, elif y else.