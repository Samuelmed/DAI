#Ejercicio 2
#Autor: Samuel Medina Gutiérrez

import random


#Funciones de ordenacion
def burbuja( matriz ):
    b = [int(x) for x in matriz]
    matriz = b
    for i in range(1, len(matriz)):
        for j in range(0,len(matriz)-i):
            if matriz[j] > matriz[j+1]:
                aux = matriz[j]
                matriz[j] = matriz [j+1]
                matriz[j+1] = aux
    return str(matriz)


def ordenacionSacudida( matriz ):
    izq = 2
    der = len(matriz) - 1
    ultimo = len(matriz) - 1

    while izq < der:
        for i in range(der, izq, -1):
            if matriz [i-1] > matriz [i]:
                aux = matriz [i]
                matriz[i] = matriz [i-1]
                matriz[i-1] = aux
                ultimo = i
    
        for j in range(izq,der):
            if matriz[j-1] > matriz[j]:
                aux = matriz[j]
                matriz[j] = matriz[j-1]
                matriz[j-1] = aux
                ultimo = j
        
        der = ultimo -1
    
    return matriz

#Funcion para generar una matriz aleatoria
def generaMatriz():
    matriz = [random.randrange(200) for i in range(100)]
    return matriz




#Comenzamos a generar una matriz

matrizAOrdenar = generaMatriz()

print (matrizAOrdenar)
print(burbuja (matrizAOrdenar))
