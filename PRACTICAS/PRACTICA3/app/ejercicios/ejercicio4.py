def fibonacci (numero):
    num = int(numero)
    if num == 1 or num == 2:
        return ' el numero buscado es 2'
    else:
        i = 1
        j = 1
        k = 1
        while k < num:
            k = k+1
            aux = i
            i = i + j
            j = aux
    return ' El número que buscas es ' + str(j)