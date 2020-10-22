#./app/app.py
from flask import Flask, url_for
from ejercicios.ejercicio2 import burbuja
from ejercicios.ejercicio3 import criba
from ejercicios.ejercicio4 import fibonacci
from ejercicios.ejercicio5 import cadena
import random
app = Flask(__name__)
          
@app.route('/')
def indice():
    return app.send_static_file('index.html')

@app.route('/ordena/<elementos>')
def ordenar(elementos):
    lista = elementos.split(',')
    
   
    burbuja(lista)

    return str(lista)

@app.route('/criba/<numero>')
def cribar(numero):
    return criba(numero)

@app.route('/fibonacci/<numero>')
def fibo(numero):
    return fibonacci(numero)

@app.route('/cadena')
def cade():
    return cadena()

#Vamos a crear una ruta para cuando no exista la ruta a la que 
#se está intentando acceder

@app.errorhandler(404)
def page_not_found(error):
    return 'Está página no ha sido encontrada',404


#Creamos la ruta para ver las imagenes vecrtoriales

@app.route('/vectorial/')
def imagen_vectorial_random():
    r = random.randrange(10,100) 
    n = random.randrange(0,3)
    l = r / (n+1)
    r = str(r)
    l = str(l)
    if n == 0:
        return '<svg>' '<circle r="' + r + ' " cx="100" cy="100" />' '</svg>' 
    elif n == 1:
        return '<svg>' '<rect x="60" y ="60" height="' + r + '" width = "' + r + '"/>' '</svg>'
    else:
        return '<svg>' '<ellipse cx="60" cy="60" rx="' + r + '" ry = " ' + l + '"/>' '</svg>'