#Práctica número 3 de la Asignatura
#Desarrollo de aplicaciones para internet.
#Autor: Samuel Medina Gutiérrez

from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify
from bson import ObjectId 
from pickleshare import * 
from ejercicios.ejercicio2 import burbuja
from ejercicios.ejercicio3 import criba
from ejercicios.ejercicio4 import fibonacci
from model import dataBase
from pymongo import MongoClient



app = Flask(__name__)
app.secret_key = 'claveSuperSecreta'


bd = dataBase()


#Conectamos con el servicio "mongo en su puerto estándar"
client = MongoClient("mongo", 27017)
db = client.SampleCollections









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


############### PRACTICA 4 ###############################

@app.route('/mongo',  methods=['GET','POST'])
def mongo():
    prueba = db.samples_friends

    
    

    if request.method == 'POST':
        titulo = request.form['title']

        episodios = prueba.find({'name': { "$regex": titulo, "$options": 'i'}})
        


        titulo = []

        for episodio in episodios:
            sumary = episodio['summary'].replace("<p>" , " ").replace("</p>" , " ")
            
            
            if episodio['image'] != None :
                tit = [episodio['name'], episodio['airdate'], episodio['airtime'], sumary,
                    episodio['image']['medium']]
            else: 
                tit = [episodio['name'], episodio['airdate'], episodio['airtime'], sumary, None]
            titulo.append(tit)


        return render_template('list.html', buscado = True, match=titulo)
    
    

    ##return str(lista_episodios)
    return render_template('list.html', buscado = False)



##Práctica 5 
@app.route('/api/capitulos', methods = ['GET', 'POST'])
def api_1():
    if request.method == 'GET':
        lista = []
        capitulos = db.samples_friends.find().sort('name')
        for capitulo in capitulos:
            lista.append({
                  'id':    str(capitulo.get('_id')), # pasa a string el ObjectId
                  'title': str(capitulo.get('name')), 
                  'airTime':  str(capitulo.get('airtime')),
                  'date':  str(capitulo.get('airdate'))
                })
        return jsonify(lista)

    if request.method == 'POST':
        name = request.form['title']
        result = db.samples_friends.insert_one({'name': name})
        capitulo = db.samples_friends.find_one({'_id':ObjectId(result.inserted_id)})
        return jsonify({
            'id':    str(capitulo.get('_id')), # pasa a string el ObjectId
            'title': capitulo.get('name'), 
            'airTime':  capitulo.get('airtime'),
            'date':  capitulo.get('airdate')
        })


@app.route('/api/capitulos/<id>', methods = ['GET', 'PUT', 'DELETE'])
def api_2(id):
    if request.method == 'GET':
        capitulo = db.samples_friends.find_one({'_id':ObjectId(id)})
        return jsonify({
            'id':    str(capitulo.get('_id')), # pasa a string el ObjectId
            'title': capitulo.get('name'), 
            'airTime':  capitulo.get('airrime'),
            'date':  capitulo.get('airdate')
        })
    if request.method == 'DELETE':
        db.samples_friend.remove({'_id':ObjectId(id)})
        return jsonify('deleted')

    if requested.method == 'PUT':
        name = request.form['name']
        
        

    

