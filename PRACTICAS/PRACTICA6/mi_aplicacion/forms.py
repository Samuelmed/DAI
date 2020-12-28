from django import forms
from mi_aplicacion.models import Libro


##Cada una de estas variables va a ser un <input>
class RegistrarLibro(forms.Form):
    titulo = forms.CharField(label='Titulo:',max_length=200)
    autor  = forms.CharField(label='Autor: ',  max_length=100)

    def registrar_libro(self):
        nuevo_libro = Libro(titulo = self.data['titulo'],
                                autor = self.data['autor'])
        nuevo_libro.save()
        return 'Registro exitoso'

class BorrarLibro(forms.Form):
    idd = forms.IntegerField(label = 'Id: ')

    def borrar_libro(self):
        Libro.objects.filter(id=self.data['idd']).delete()
        return 'Borrado Exitoso'