from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def test_template(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'test.html', context)

def log(request):
    context = {}
    return render(request, 'login.html', context)