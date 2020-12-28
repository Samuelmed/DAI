from django.shortcuts import render, redirect
from .forms import RegistrarLibro, BorrarLibro
from .models import Libro

# Create your views here.
def index(request):
    mis_libros = Libro.objects.all()
    if request.method == 'POST':
        register_form = RegistrarLibro(request.POST)
        if register_form.is_valid():
            success = register_form.registrar_libro()
            return redirect('./')
    
    if request.method == 'DELETE':
        delete_form = BorrarLibro(request.DELETE)
        if delete_form.is_valid():
            success = delete_form.borrar_libro()
            return redirect('./')
    else:
        register_form = RegistrarLibro()
        delete_form = BorrarLibro()
        return render(request, 'forms/mi_form.html', {'register_form': register_form, 'libros':mis_libros,
                                                        'delete_form': delete_form})

def test_template(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'index.html', context)

