#Práctica número 3 de la Asignatura
#Desarrollo de aplicaciones para internet.
#Autor: Samuel Medina Gutiérrez

from flask import Flask, render_template, request, flash, redirect, url_for

##Para una aproximacion inicial, vamos a usar una matriz como base de datos
baseUsuario =[['admin', 'secret']]

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods =['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['username']
        pssw = request.form['password']  
        if  not [name, pssw] in baseUsuario:
            error = 'Credenciales incorrectas'
        else:
            flash('Te has logeado correctamente')
            return redirect (url_for('index'))
    return render_template('login.html', error = error)

@app.route('/signup', methods = ["GET" , "POST"])
def singup():
    error = None
    if request.method == 'POST':
        name = request.form['username']
        pssw = request.form['password']
        if not name or not pssw:
            error = "Has introducido una cadena vacia"
        else:  
            baseUsuario.append([name, pssw])
            flash('Te has registrado correctamente, por favor intente acceder')
            return redirect (url_for('index'))
       
    return render_template ('signup.html', error = error)


