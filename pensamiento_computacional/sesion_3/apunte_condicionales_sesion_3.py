# Condicionales

# 1.4 Ejercicio
"""
Debemos calcular el pago a un trabajador. 
- El cálculo debe hacerse por la cantidad de horas trabajadas. 
- Le vamos a pedir al usuario por pantalla la cantidad de horas que trabaja y cuánto vale cada hora de trabajo.
"""
hs_trabajadas = int(input("Ingresá tus hs trabajadas: "))
valor_hs_trabajo = int(input("Ingresá el valor de tu hs de trabajo: "))
sueldo_final = hs_trabajadas  * valor_hs_trabajo
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
tiene_hijos = input("¿Tenés hijos? Respondé con Si o No ")
if tiene_hijos == "si":
    sueldo_final *= 0.20 # aumento del 20% por tener hijos
elif hs_trabajadas > 30:
    sueldo_final *= 0.10 # # aumento del 10% por +30 hs trabajadas
else: 
    sueldo_final

print(f"Tu sueldo final es ", sueldo_final)








