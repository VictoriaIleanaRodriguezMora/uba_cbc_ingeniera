1ro me estaba equivocando en esto: 
```py
completo = open('pensamiento_computacional/sesion_8/apunte/datosCompletos.csv', 'w') # Crea el archivo datosCompletos
```
no estaba poniendo `datosCompletos.csv`, estaba poniendo `comma_separated_value.py`

     
Después, me estaba equivocando en que en el código estaba haciendo: `a[i] = a[i].split(';') # Arma tabla quitando ;`, estaba spliteando en **`;`** y mis csv estaban escritos con **`,`**, por eso me daba error