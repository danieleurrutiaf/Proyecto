from django.shortcuts import render

from .models import Usuario,Genero

# Create your views here.


def index(request): 
    context = {}
    return render(request, 'taller1/index.html', context) 

def base(request): 
    context = {}
    return render(request, 'taller1/base.html', context) 

def contacto(request):
    context = {}
    return render(request, 'taller1/contacto.html', context)

def noticias(request):
    Usuarios= Usuario.objects.all()
    context = {"Usuarios":Usuarios}
    return render(request, 'taller1/noticias.html', context)

def catalogo(request):
    context = {}
    return render(request, 'taller1/catalogo.html', context)

def carrito(request):
    context = {}
    return render(request, 'taller1/carrito.html', context)
#Sercicios

def servicio1(request):
    context = {}
    return render(request, 'taller1/Servicios/servicio1.html', context)
def servicio2(request):
    context = {}
    return render(request, 'taller1/Servicios/servicio2.html', context)
def servicio3(request):
    context = {}
    return render(request, 'taller1/Servicios/servicio3.html', context)
def servicio4(request):
    context = {}
    return render(request, 'taller1/Servicios/servicio4.html', context)
def servicio5(request):
    context = {}
    return render(request, 'taller1/Servicios/servicio5.html', context)
def servicio6(request):
    context = {}
    return render(request, 'taller1/Servicios/servicio6.html', context)

def crud(request):
    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios}
    return render(request, 'taller1/usuarios_list.html', context)

def usuariosAdd(request):
    if request.method is not "POST":

        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request, 'taller1/usuariosAdd.html', context)