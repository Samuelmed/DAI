import random

def cadena():
    #generamos un aleatorio entre 1 y 20
    limite =random.randrange(20)
    cad = []
    for i in range (limite):
        rand = random.randrange(100)
        if rand % 2 == 0:
            cad.append('[')
        else:
            cad.append(']')
    
    #Ahora que ya hemos generado la cadena
    #la recorremos
    #En este contador almacenamos apariciones
    j = 0
    for i in range(len(cad)):
        if cad[i] == '[':
            j = j+1
        else:
            j= j-1

        if j < 0:
            return str(cad) + ' Cadena no valida'
    return str(cad) + ' Cadena valida'