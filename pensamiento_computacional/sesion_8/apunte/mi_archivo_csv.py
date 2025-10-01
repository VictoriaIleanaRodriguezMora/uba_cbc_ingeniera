# Ordenar de mayor a menor los puntajes. 4ta columna

datos_unificados = open('pensamiento_computacional/sesion_8/apunte/datos_unificados.csv', 'w')
datos_finales = []

datos1 = open('pensamiento_computacional/sesion_8/apunte/datos1.csv', 'r',  encoding='utf-8')
datos1_array_de_lineas = datos1.readlines() # array donde c posicion es un string con el contenido de la linea
# print(datos1_array_de_lineas) # 'Luciana,juárez,santiago del estero,95\n',]
datos2 = open('pensamiento_computacional/sesion_8/apunte/datos2.csv', 'r',  encoding='utf-8')
datos2_array_de_lineas = datos2.readlines()



for linea in datos1_array_de_lineas:
    linea = linea.strip('\n') # Quito el \n de cada línea.
    # print(linea) # Luciana,juárez,santiago del estero,95
    linea = linea.split(',')
    # print(linea) # ['Luciana', 'juárez', 'santiago del estero', '95'] | ['Julián', 'manzur', 'santiago del estero', '98']
    linea[3] = int(linea[3])
    datos_finales.append(linea) # Esto no funciona --> datos_finales += linea
# print(datos_finales) # [['Luciana', 'juárez', 'santiago del estero', 95], ['Julián', 'manzur', 'santiago del estero', 98],

# datos_finales.sort() # Asc por la primer posicion, pero yo quiero que ordene por las notas
# print(datos_finales) # [['Anabel', 'llanes', 'mendoza', '83'], ['Julián', 'manzur', 'santiago del estero', '98'], 

def ordenarPorPuntaje(alumno):
    # print('alumno', alumno)
    return alumno[3]

datos_finales.sort(key=ordenarPorPuntaje, reverse=True)
print(datos_finales) # [['Julián', 'manzur', 'santiago del estero', 98], ['Luciana', 'juárez', 'santiago del estero', 95], ['Rogelio', 'linares', 'córdoba', 88], ['Anabel', 'llanes', 'mendoza', 83], ['Mariano', 'álvarez', 'san luis', 68]]

# Ya tengo los datos ordenados, y filtrados. Ahora los tengo que escribir en el archivo.
# Hay que tener cuidado al escribir en archivos .csv, porque debo guardarlos apropiadamente. Valores separados por coma Y SALTO DE LINEA

for item in datos_finales:
    item[3] = str(item[3])
    # join une las posiciones de un arreglo, con lo que yo le paso. array a string = "algo".join([])
    # le paso item, porque datos_finales es un array, de arrays. Entonces item, es un array. join puede operar sobre el
    # [['Julián', 'manzur', 'santiago del estero', 98], ['Luciana', 'juárez', 'santiago del estero', 95],
    item_unido_a_str_con_n = (",".join(item) + '\n')
    print(item_unido_a_str_con_n) # Julián,manzur,santiago del estero,98
    datos_unificados.write(item_unido_a_str_con_n)
    
datos_unificados.close()