from django.shortcuts import render

# Create your views here.


def index(request): 
    context = {}
    return render(request, 'taller1/index.html', context) 

def contacto(request):
    context = {}
    return render(request, 'taller1/contacto.html', context)

def noticias(request):
    context = {}
    return render(request, 'taller1/noticias.html', context)

def catalogo(request):
    context = {}
    return render(request, 'taller1/catalogo.html', context)

def carrito(request):
    context = {}
    return render(request, 'taller1/carrito.html', context)

def proyecto1(request):
    context = {}
    return render(request, 'taller1/proyecto1.html', context)