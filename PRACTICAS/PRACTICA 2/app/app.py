#./app/app.py
from flask import Flask, url_for
from ejercicio2 import burbuja
import re
app = Flask(__name__)
          
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ordena/<elementos>')
def ordenar(elementos):
    print(url_for('static', filename='style.css'))
    lista = re.findall('[0-9]',elementos)
    aux = []

    for i in range(len(lista)):
        aux.append(int(lista[i]))
   
    burbuja(aux)
    final = [str(x) for x in aux]
    final2 = "".join(final)
    return final2

with app.test_request_context():
    url_for('static', filename='style.css')