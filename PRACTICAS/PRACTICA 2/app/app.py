#./app/app.py
from flask import Flask, url_for
from ejercicios.ejercicio2 import burbuja
from ejercicios.ejercicio3 import criba
from ejercicios.ejercicio4 import fibonacci
from ejercicios.ejercicio5 import cadena
import random
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

@app.route('/nombre/<nom>')
def es_un_nombre(nom):
    es_nombre = bool(re.match(r"[\w\s]+[A-Z]", nom))
    if (es_nombre):
        return "El nombre está bien escrito"
    else:
        return "El nombre no está bien escrito"

@app.route('/email/<em>')
def es_un_email(em):
    es_email = bool(re.match(r"^[._a-z0-9-]+@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$", em))
    if (es_email):
        return "El email está bien escrito"
    else:
        return "El email no está bien escrito"

@app.route('/tarjeta/<num>')
def es_una_tarjeta(num):
    es_tarjeta = bool(re.match(r"^\d{4}([\ \-]?)\d{4}\1\d{4}\1\d{4}$", nums))
    if (es_tarjeta):
        return "El número de tarjeta está bien escrito"
    else:
        return "El número de tarjeta no está bien escrito"
#Vamos a crear una ruta para cuando no exista la ruta a la que 
#se está intentando acceder

@app.errorhandler(404)
def page_not_found(error):
    return 'Está página no ha sido encontrada',404


#Creamos la ruta para ver las imagenes vecrtoriales

@app.route('/vectorial/')
def imagen_vectorial_random():
    r = random.randrange(10,100) 
    n = random.randrange(0,21)
    l = r / (n+1)
    r = str(r)
    l = str(l)
    if n % 4 ==  0:
        color = "blue"
    elif n % 4 == 1:
        color = "red"
    elif n % 4 == 2:
        color = "green"
    else:
        color = "yellow"

    if n % 3 == 0:
        return '<svg>' '<circle r="' + r + ' " cx="100" cy="100" fill="' + color+ '" />' '</svg>' 
    elif n % 3 == 1:
        return '<svg>' '<rect x="60" y ="60" height="' + r + '" width = "' + r + '" fill="' + color + '"/>' '</svg>'
    else:
        return '<svg>' '<ellipse cx="60" cy="60" rx="' + r + '" ry = " ' + l + '" fill="' + color + '"/>' '</svg>'