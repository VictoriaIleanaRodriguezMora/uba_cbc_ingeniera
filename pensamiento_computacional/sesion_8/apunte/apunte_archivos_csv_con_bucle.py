# Ordenar de mayor a menor los puntajes. 4ta columna
datos_unificados = open('pensamiento_computacional/sesion_8/apunte/datos_unificados.csv', 'w')
datos_finales = []

for i in range(1, 4):
    all_data = open('pensamiento_computacional/sesion_8/apunte/datos' + str(i) + '.csv')
    lines_all_data = all_data.readlines()
    all_data.close()

    for linea in lines_all_data:
        linea = linea.strip('\n')
        linea = linea.split(',')
        linea[3] = int(linea[3])
        datos_finales.append(linea) 

   

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