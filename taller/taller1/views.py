from django.shortcuts import render , redirect, get_object_or_404
from .models import Usuario,Genero

from .forms import UsuarioForm

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
    context = {"Usuarios": usuarios}
    return render(request, 'taller1/usuarios_list.html', context)


def UsuarioAdd(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'taller1/usuarios_add.html', {'form': form})  # Redirige a la página principal o a donde corresponda después de agregar el usuario
    else:
        form = UsuarioForm()

    return render(request, 'taller1/usuarios_add.html', {'form': form}) 

def Usuario_del(request, pk):
    mensajes=[]
    errores=[]
    usuarios=Usuario.objects.all()
    try:
        usuario= Usuario.objects.get(rut=pk)
        context=()
        if usuario:
            usuario.delete()
            mensajes.append("Bien, datos eliminados...")
            context = {'usuarios': usuarios, 'mensajes': mensajes, 'errores': errores}
            return render(request, 'taller1/usuarios_list.html', context)
    except:
        print("Error, rut no existe...")
        usuarios= Usuario.objects.all()
        mensaje= "Error, rut no existe..."
        context={'mensaje': mensaje, 'usuarios': usuarios,}
        return render(request, 'taller1/usuarios_list.html', context)    

    
    













    

