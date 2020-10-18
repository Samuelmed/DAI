#Ejercicio 1 propouesto en DAI
#autor: Samuel Medina Gutiérrez

import random

#Generamos el número random que queremos que el usuario adivine
numero = random.randrange(100)
print ( numero )

print ("Por favor intente adivinar el número que tengo en mente:")

posible = int(input())


    

while posible != numero:
    if posible > numero :
        print ( "es mayor" )
        posible = int(input())
    else :
        print ( "es menor" )
        posible = int(input())
else:
    print ( "¡Felicidades, es el número correcto!" )