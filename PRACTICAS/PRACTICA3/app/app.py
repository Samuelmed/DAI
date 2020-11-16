#Práctica número 3 de la Asignatura
#Desarrollo de aplicaciones para internet.
#Autor: Samuel Medina Gutiérrez

from flask import Flask, render_template, request, flash, redirect, url_for, session
from pickleshare import * 
from ejercicios.ejercicio2 import burbuja
from ejercicios.ejercicio3 import criba
from ejercicios.ejercicio4 import fibonacci
from model import dataBase


app = Flask(__name__)
app.secret_key = 'claveSuperSecreta'


##Añadimos el primer usuario "Admin, secret"

bd = dataBase()







@app.route('/')
@app.route('/index')
def index():
    if not session.get('visited'):
        session['visited'] = []
    if not session.get('logeado'):
        session['logeado'] = False
        if not session.get('usuActual'):
            session['usuActual'] = None

    return render_template('index.html', urls = session['visited'], logeado = session['logeado'])

@app.route('/login', methods =['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['username']
        pssw = request.form['password']  
        if  name in bd.getKeys() and bd.getPssw(name) == pssw:
            flash('Te has logeado correctamente')
            session['logeado'] = True  
            session['usuActual'] = name
            return redirect (url_for('index'))    
        else:
            error = 'Credenciales incorrectas'
    return render_template('login.html', error = error)

@app.route('/signup', methods = ["GET" , "POST"])
def singup():
    error = None
    if request.method == 'POST':
        name = request.form['username']
        pssw = request.form['password']
        if not name or not pssw:
            error = "Has introducido una cadena vacia"
        elif name in bd.getKeys():
            error = "Lo siento, ya existe este usuario"
        else:  
            bd.aniade(name,pssw)
            flash('Te has registrado correctamente, por favor intente acceder')
            return redirect (url_for('index'))
       
    return render_template ('signup.html', error = error)

##Cuandio un usuario se desloguee redirigimos al index 

@app.route('/logout')
def logout():
    session['logeado'] = False
    return redirect (url_for('index'))

@app.route('/adddata', methods = ["GET" , "POST"])
def aniade():
    error = None

    usuarioAct = session['usuActual']
    infor = bd.getInformacion(usuarioAct)
    name = infor[0]
    surname = infor[1] 
    age = infor[2]
    if request.method == 'POST':
        usuarioAct = session['usuActual']
        name = request.form['name']
        surname = request.form['surname']
        age = request.form['age']

        bd.aniadirInformacion(usuarioAct,name,surname,age)



        return redirect(url_for('index'))
    return render_template('aniade.html', error = error, nombre = name, apellido = surname, edad = age)

@app.route('/userdata')
def mostrar():
    usuarioAct = session['usuActual']
    infor = bd.getInformacion(usuarioAct)
    name = infor[0]
    surname = infor[1] 
    age = infor[2]
    return render_template('userdata.html', nombre = name, apellido = surname, edad = age)

@app.route('/ejer1' , methods=['GET','POST'])
def mostrarEjer1():
    if request.method == 'POST':
        numeros = request.form['numbers']
        lista = numeros.split(',')
        ordenado =burbuja(lista)
        return render_template('ejer1.html', ordenado=True, lista=ordenado)
    return render_template('ejer1.html', ordenado=False)

@app.route('/ejer2' , methods=['GET','POST'])
def mostrarEjer2():
    if request.method == 'POST':
        numero = request.form['number']
        lista =criba(numero)
        return render_template('ejer2.html', ordenado=True, lista=lista)
    return render_template('ejer2.html', ordenado=False)

@app.route('/ejer3' , methods=['GET','POST'])
def mostrarEjer3():
    if request.method == 'POST':
        numero = request.form['number']
        numero = fibonacci(numero)
        return render_template('ejer3.html', ordenado=True, lista=numero)
    return render_template('ejer3.html', ordenado=False)


@app.after_request
def visited_url(response):
    if not session.get('visited'):
        session['visited'] = []
    session['visited'].append(request.url)
    if len(session['visited']) > 3:
        session['visited'].pop(0)
    session.modified = True

    return (response)

@app.context_processor
def aniade_url():
    if session.get('visited'):
        lurls = session['visited']
    else:
        lurls=[]
    return dict(urls = lurls)

@app.context_processor
def log():
    logeados = session['logeado']
    return dict(logeado=logeados)

