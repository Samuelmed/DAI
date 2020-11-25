#En este módulo tendremos todas las funciones relaciondas con la base de datos

from pickleshare import * 

class dataBase:
    
    def __init__(self):
        self.db = PickleShareDB('Usuarios')

    def aniade(self, nombre, password):
        self.db[nombre] = dict()
        self.db[nombre]['pass'] = password
        self.db[nombre]['name'] = ''
        self.db[nombre]['surname'] = ' '
        self.db[nombre]['age'] = '  '
        self.db[nombre] = self.db[nombre]
    
    def getKeys(self):
        return self.db.keys()

    def aniadirInformacion(self, usuario, nombre, apellidos, edad):
        self.db[usuario]['name'] = nombre
        self.db[usuario]['surname'] = apellidos
        self.db[usuario]['age'] = edad
        self.db[usuario] = self.db[usuario]

    def getInformacion(self, usuario):
        informacion = []
        informacion.append(self.db[usuario]['name']) 
        informacion.append(self.db[usuario]['surname'])
        informacion.append(self.db[usuario]['age'])
        
        return informacion

    def getPssw(self, usuario):
        return self.db[usuario]['pass']
