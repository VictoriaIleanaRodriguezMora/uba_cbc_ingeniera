# Archivos

# No hice modificacion. Solo manipula la vista del archivo. Porque en la variable tengo acceso al contenido. Pero el archivo ya cerró, no hay peligro.

# Abrir archivo - open()
# open("rutadelarchivo/archivo.txt") devuelve la llave para trabajar con el mismo archivo
archivo_cancion = open("pensamiento_computacional/sesion_8/sesion_8.md")

# Hay muchas formas de manipular un archivo
lineas = archivo_cancion.readlines() # Lista de cadenas, strings. Donde cada string es una linea del archivo 
# print("lineas", lineas)

# print(lineas) # ['Loving him is like driving a new Maserati down a dead end street\n', '',...]

# Tiene explícito el caracter /n

# Cerrar el archivo
archivo_cancion.close()

contador = 0
for linea in lineas:
    if 'red' in linea:
        contador += 1

# print(f"La palabra red aparece {contador} veces")

# Archivos CSV



# 1er paso
personas_csv = open('pensamiento_computacional/sesion_8/personas.csv')
# 2do paso. Guardo la referencia en memoria, para usarla
personas_lineas = personas_csv.readlines()
# 3er paso
personas_csv.close()

# print(personas_lineas) # ['juan;30\n', 'maria;20\n', 'pedro;18\n', 'manuel;34\n', 'ana;26\n', 'milagros;28']

def limpiar_personas(persona):
    persona = persona.strip('\n') # Strip quita de un string lo que le paso por parametro, por defecto los espacios. ['juan;30']
    persona = persona.split(';') # Split divide un string, y genera un array, donde encuentre lo que le pasé por parametro
    return persona

# Se le pasa el 2do parametro de map, cómo argumento a limpiar_personas
# envuelvo todo en un list, porque map retorna un mapa, y yo quiero tratarlo como una lista
personas_limpio = list(map(limpiar_personas, personas_lineas)) # map(fn, obj iterable)
print(personas_limpio) # [['juan', '30'], ['maria', '20'], ['pedro', '18'], ['manuel', '34'], ['ana', '26'], ['milagros', '28']]

suma_edades = 0
contador_personas = 0
# Como lo habria hecho yo
"""
for person in personas_limpio:
    print(person[0], person[1])
    suma_edades += int(person[1]) # TypeError: unsupported operand type(s) for +=: 'int' and 'str'
    contador_personas += 1
print(f'El promedio es {suma_edades / contador_personas}')
"""
# 
for person in personas_limpio:
    [nombre, edad] = person # ❗ Desestructuracion
    suma_edades += int(edad) # TypeError: unsupported operand type(s) for +=: 'int' and 'str'

print(f'La suma de las edades es {suma_edades}')
print(f'El promedio es {suma_edades / len(personas_limpio)}')



