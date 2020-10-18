#Ejercicio 3
#Criba de Erastotenes
# Autor: Samuel Medina Gutiérrez

#pedimos el número para el que se quiere listar los primos por debajo
#de este

print ( "Elija el número que desee para listar todos los primos por debajo de este: ")
tope = int(input())

lista = [i for i in range(2,tope+1)]
listaAux= []
print(lista)
j=0

while lista[j]*lista[j] < tope:
    print (j)
    
    numero = lista[j]
    j = j+1
    for i in range(len(lista)):
        if lista[i] % numero == 0:
            if lista [i] != numero:
                listaAux.append(lista[i])

    for i in range(len(listaAux)):
        lista.remove(listaAux[i])
        
    while len(listaAux) != 0:
        listaAux.pop()


print ( "Los primos hasta ese número son: ")
print (lista)