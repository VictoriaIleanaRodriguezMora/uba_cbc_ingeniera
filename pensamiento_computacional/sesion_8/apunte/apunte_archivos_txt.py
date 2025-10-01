vaca_txt = open('pensamiento_computacional/sesion_8/apunte/arch1.txt', 'r+')

t = vaca_txt.readline()
print(t)

t = input('Ingresá un texto con vaca: ')
while (t.lower()).count('vaca') == 0:
    t = input('Ingresá un texto con vaca: ')

vaca_txt.write(t + '\n')
vaca_txt.close()

vaca_txt = open('pensamiento_computacional/sesion_8/apunte/arch1.txt')

todas = vaca_txt.readlines()
for linea in todas:
    print(linea.strip('\n'))

vaca_txt.close()