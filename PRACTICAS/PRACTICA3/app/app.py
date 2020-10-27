#Práctica número 3 de la Asignatura
#Desarrollo de aplicaciones para internet.
#Autor: Samuel Medina Gutiérrez

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    name = 'Rosalia'
    return render_template('index.html')