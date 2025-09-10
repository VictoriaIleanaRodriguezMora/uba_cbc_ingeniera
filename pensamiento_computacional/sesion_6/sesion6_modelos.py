# Respuestas a los módelos de parcial
# Ejemplo 1 - Tema 7
# ¿Qué resultado muestra el siguiente programa?
a=2
b=1
c=4
d=-6
print(float(a**b+abs(d)+c/a)) 
float(a**b+abs(d)+c/a)
float(2**1 + abs(-6) + 4/2)
#        2 + 6 + 2

# 2**1 = 2
# abs(-6) = 6
# 4/2 = 2

### RTA: (3) 10.0 

# 0207 ¿Qué programa evalúa más condiciones en total?
### 1 -
categoria='hilo'
clase='algodón'
color='blanco'
if categoria in ('hilo','cinta'):
        if clase=='seda':
                print('Tengo')
        if categoria=='aguja':
                print('fina o gruesa?')
        if categoria=='botón':
                if color=='azul' or color=='plata':
                        print('Tengo')
        if categoria=='cinta':
                if color in ('oro', 'plata', 'peltr'):
                        print('Hay')
        if categoria=='hilo':
         print('raso o seda')
        elif clase=='plástico':
         print('Económico')
        elif clase=='cristal':
         print('Caro') 

### 2
categoria='hilo'
clase='algodón'
color='blanco'
if categoria in ('hilo','cinta'):
 if clase !='seda':
         print('Tengo')
elif categoria=='aguja':
 print('fina o gruesa?')
elif categoria=='botón':
 if color=='azul' or color=='plata':
         print('Tengo')
elif categoria=='cinta':
 if color in ('oro', 'plata', 'peltr'):
         print('Hay')
else:
 if clase=='plástico':
         print('Económico')
 elif clase=='cristal':
         print('Caro') 

### 3
categoria='hilo'
clase='algodón'
color='blanco'
if categoria in ('hilo','cinta'):
 if clase=='seda':
         print('Tengo')
 else:
         print('No tengo')
elif categoria=='aguja':
 print('fina o gruesa?')
else:
 if color=='azul' or color=='plata':
         print('Tengo')

### 4
categoria='hilo'
clase='algodón'
color='blanco'
if categoria in ('hilo','cinta'):
 if clase=='seda':
         print('Tengo')
 else:
         print('No tengo')
if categoria=='aguja':
 print('fina o gruesa?')
else:
 if color=='azul' or color=='plata':
        print('Tengo')

### RTA: La opcion 1 evalúa más condiciones en total ✅


# 0307 ¿Qué muestra por pantalla el siguiente programa?
valores=[1,4,2,0,3]
ejemplos=['y','ir','bajo','abajo','objetivo', 'acabáremos']
print('Ejemplos de vocablos con n vocales')
for num in valores:
        # print("num",num)
        print(num, ejemplos[num])
# RTA: Opcion 4 ✅


# 0507 ¿Qué muestra por pantalla el siguiente programa?
pal='SUERTE'
for i in range(len(pal)):
        corre=' '*(len(pal)-(i+1))
        print(corre+pal[len(pal)-(i+1):])

# RTA: Opcion 4 ✅


# ¿Qué muestra el siguiente programa?
a=[1,3,0,2]
b=['ana','pedro','luis','emilia','li']
c=[]
for num in a:
        nom=b[num]
        c.append(len(nom)//2)
print(c)
# RTA: Opcion 4 - [2, 3, 1, 2] ✅

# 0707 ¿Qué programa ejecuta más veces el cuerpo del bucle?
# Desde 10, hasta 0 sin incluirlo. De a paso -5. Solo entra 2 veces al bucle 10, 5
for i in range(len('mamarracho'),0,-5):
        j=0
        print(i) # 10 - 5
# Ejecuta 5 veces
for i in [1,2,6,7,8]:
        j=0

# lo ejecuta 1 sola vez
i=100
j=2
while j>0:
        j-=3

# 9 veces ejecuta. me confundio el 'car'
for car in 'argentina':
        i=0


# 0807 ¿Qué función es adecuada para el siguiente programa?
# """
def cociente(n1,n2):
        if n1==0:
         resultado=0
        else:
         resultado=n2/n1
         return resultado

lista=[10,0,100]
factor=[5,6,4]
for i in range(len(lista)):
        print(cociente(lista[i],factor[i]))
# """
# Debe mostrar la siguiente salida:
# 0.5
# 0
# 0.04


a = 1
a += 2
print("aaaaa ", (a ))