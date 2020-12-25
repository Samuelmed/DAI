# mi_aplicacion/models.py
from django.db import models
from django.utils import timezone
from django import forms

class Librero(models.Manager):
	def crear_libro(self, titulo, autor):
		libro = self.crear_libro(titulo, autor)
		return libro

class Libro(models.Model):
  título = models.CharField(max_length=200, primary_key=True)
  autor  = models.CharField(max_length=100)

  objects = Librero()

  @classmethod
  def create(cls, titulo, autor):
  	libro = cls(titulo=titulo, autor=autor)
  	return libro


class Prestamo(models.Model):
  libro   = models.ForeignKey(Libro, on_delete=models.CASCADE)
  fecha   = models.DateField(default=timezone.now)
  usuario = models.CharField(max_length=100)



#MODIFICACIONES BD


def Nuevo_Libro(titulo, autor):
	libro = Libro.objects.crear_libro(titulo, autor)

def Nuevo_Prestamo(libro, usuario):
	libro = Libro.objects.crear_libro()


  

#FORMULARIOS

class LibroForm(forms.Form):
	titulo = forms.CharField(required=True)
	autor = forms.CharField(required=True)


class PrestamoForm(forms.Form):
	libro = forms.CharField()
	usuario = forms.CharField(max_length=100)