# Condicionales

# 1.4 Ejercicio
"""
Debemos calcular el pago a un trabajador. 
- El cálculo debe hacerse por la cantidad de horas trabajadas. 
- Le vamos a pedir al usuario por pantalla la cantidad de horas que trabaja y cuánto vale cada hora de trabajo.
"""

"""
Ahora imaginemos que en la empresa se decide abonar un 
- plus fijo de guardería a todo trabajador que tiene hijos. 
- Y pagar un 10% de incentivo a todo trabajador que haya hecho 30 horas o más y NO reciba el plus por guardería.
Es decir, antes el cálculo era simplemente cant_horas * valor_hora, pero ahora se abren 4 casos posibles para calcular el sueldo del trabajador. No tenemos un solo modelo o caso de liquidación, sino varios:
* Trabajador con menos de 30 horas y sin hijos total = cant_horas * valor_hora
* Trabajador con 30 horas o más y sin hijos total = cant_horas * valor_hora * 1.1
* Trabajador con menos de 30 horas y con hijos total = cant_horas * valor_hora + plus_fijo
* Trabajador con 30 horas o más y con hijos total = cant_horas * valor_hora + plus_fijo
"""
"""
hs_trabajadas = int(input("Ingresá tus hs trabajadas: "))
valor_hs_trabajo = int(input("Ingresá el valor de tu hs de trabajo: "))
sueldo_final = hs_trabajadas  * valor_hs_trabajo
tiene_hijos = input("¿Tenés hijos? Respondé con Si o No ")
if tiene_hijos == "si":
    sueldo_final *= 0.20 # aumento del 20% por tener hijos
elif hs_trabajadas > 30:
    sueldo_final *= 0.10 # # aumento del 10% por +30 hs trabajadas
else: 
    sueldo_final

print(f"Tu sueldo final es ", sueldo_final)
"""


# 6. ✅cEscribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con ese valor. Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”.
# Extra: ¿Cómo harían para que el programa quede generalizado para cualquier límite, a elección del usuario, y no solo para 100?.

"""
def determinar_sumar(num_a, num_b, limite):
    if ((num_a + num_b) < limite ):
        print(f"A {num_a} + {num_b} = {num_a + num_b}. Le faltan {limite - (num_a + num_b)} para llegar a {limite}")
    else:
        print(f"La suma da igual que el límite")

determinar_sumar(5, 5, 10)
determinar_sumar(5, 5, 100)
"""

# 7. ✅ Se tienen letras para representar las estaciones del año:
"""
● V para verano
● O para otoño
● I para invierno 
● P para primavera
Crear una función que dada una letra, imprima por pantalla la estación del año que representa (es decir, si se ingresa V se mostrará por pantalla el mensaje “Verano”). En caso de no representar a ninguna estación mostrar un mensaje que diga “error”. Probar la función creada llamándola con A, P, O, B, V e I.
"""

"""
def estaciones_anio(letra):
    if(letra == "V"):
        print("Verano")
    elif(letra == "O"):
        print("Otoño")
    elif(letra == "I"):
        print("Invierno")
    elif(letra == "P"):
        print("Primavera")
    else:
        print("Error")

estaciones_anio("A")
estaciones_anio("P")
estaciones_anio("O")
estaciones_anio("B")
estaciones_anio("V")
"""

# Estructuras de control iterativas

# 8. Se quiere hacer un programa para enseñar a unos niños a contar. Crear una función que reciba un número entero e imprima por pantalla los números del 1 hasta ese número con la estructura de control iterativa for.
"""
def aprender_sumar(nro):
    rango_nros = range(1, nro + 1)
    for num in rango_nros:
        print(f"Número: {num}")

aprender_sumar(17)
"""

# 9. Se quiere mejorar el programa para enseñar matemáticas pensado en el ejercicio anterior. Ahora se necesita una funcionalidad que permita a los niños aprender las tablas. Crear una función que reciba un número entero e imprima por pantalla la tabla de ese número del 1 al 10.
"""
def aprender_tablas(nro):
    rango_nros = range(1, 11)
    for num in rango_nros:
        print(f"Tabla del {nro} --> {nro} * {num}: {num * nro}")

aprender_tablas(2)
"""


# 10. Crear una función que simule un cumpleaños: que dado un entero imprima “Que los cumplas feliz” esa cantidad de veces.
"""
def saludar_cumpleanios(nro_entero):
    rango_a_saludar = range(1, nro_entero + 1)
    for num in rango_a_saludar:
        print(f"Que los cumplas feliz {num}")

saludar_cumpleanios(5)
"""

# 11. En un almacén están buscando la forma de hacer los cobros más automáticamente. Para esto, se nos pide crear una función que reciba un número entero que representa lo que hay que cobrar, le pida al usuario ingresar un monto, y se vaya mostrando por pantalla cuánto falta para completar el pago. Repetir este proceso hasta que la deuda sea 0 o menor. Por ejemplo, si se recibe el monto 30:
"""
> El importe a pagar es de 30 pesos. Por favor, ingrese un monto.
> 10
> El importe a pagar es de 20 pesos. Por favor, ingrese un monto.
> 15
> El importe a pagar es de 5 pesos. Por favor, ingrese un monto.
> 5
"""

def ejercicio_11():
    monto_total = int(input("Cuanto debe pagar? "))
    monto_pagado = int(input("Ingresé el monto que desea pagar "))
    cuanto_debe = monto_total - monto_pagado
    while(monto_total > cuanto_debe):
        print(f"Usd debe {cuanto_debe}. ")
        monto_pagado = int(input("Porfavor, ingrese el monto faltante "))
    print("Usd ya pagó todo lo que debía ")

ejercicio_11()










