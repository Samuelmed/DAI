#./app/app.py
from flask import Flask, url_for
from ejercicios.ejercicio2 import burbuja
from ejercicios.ejercicio3 import criba
from ejercicios.ejercicio4 import fibonacci
from ejercicios.ejercicio5 import cadena
import re
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