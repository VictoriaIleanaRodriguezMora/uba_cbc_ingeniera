datos_unificados = open('pensamiento_computacional/sesion_8/apunte/datos_unificados.csv', 'w')
datos_finales = []

datos1 = open('pensamiento_computacional/sesion_8/apunte/datos1.csv', 'r',  encoding='utf-8')
datos1_array_de_lineas = datos1.readlines() # array donde c posicion es un string con el contenido de la linea
# print(datos1_array_de_lineas) # 'Luciana,juÃ¡rez,santiago del estero,95\n',]

for linea in datos1_array_de_lineas:
    linea = linea.strip('\n') # Quito el \n de cada línea.
    # print(linea) # Luciana,juÃ¡rez,santiago del estero,95
    linea = linea.split(',')
    # print(linea) # ['Luciana', 'juÃ¡rez', 'santiago del estero', '95']
    datos_finales.append(linea) # datos_finales += linea
print(datos_finales) # [['Luciana', 'juárez', 'santiago del estero', '95'],[]]