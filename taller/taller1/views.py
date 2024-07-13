from django.shortcuts import render , redirect, get_object_or_404
from .models import Usuario,Genero, Servicio, Mecanico
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, ServicioForm, MecanicoForm
from django.contrib import messages

@login_required
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

def servicio_detalle(request): 
    context = {}
    return render(request, 'taller1/servicio_detalle.html', context) 

def carrito(request):
    context = {}
    return render(request, 'taller1/carrito.html', context)

def crud(request):
    usuarios = Usuario.objects.all()
    mecanicos = Mecanico.objects.all()
    context = {
        "Usuarios": usuarios,
        "Mecanicos": mecanicos
    }
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
    try:
        # Obtén el objeto Servicio que deseas eliminar
        usuario = get_object_or_404(Usuario, rut=pk)
        usuario.delete()  # Elimina el objeto

        # Mensaje de éxito
        messages.success(request, "Bien, el usuario seleccionado eliminado...")
    except Usuario.DoesNotExist:
        # Mensaje de error si el servicio no existe
        messages.error(request, "Error, el usuario no existe...")

    # Redirige al usuario a la lista de servicios
    return redirect('crud')    

    
def Usuario_edit(request, pk):
    usuario = get_object_or_404(Usuario, rut=pk)  # Utiliza get_object_or_404 para manejar usuarios no existentes
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():  # Asegúrate de que el formulario es válido antes de guardar
            form.save()
            mensaje = "Bien, datos actualizados..."
            return redirect('Usuario_edit', pk=usuario.rut)  # Redirige a una página de detalle o lista después de guardar
        else:
            mensaje = "Error, datos no válidos."
    else:
        form = UsuarioForm(instance=usuario)
        mensaje = ""

    context = {'usuario': usuario, 'form': form, 'mensaje': mensaje}
    return render(request, 'taller1/usuarios_edit.html', context)


def menu(request):
    request.session["usuario"]="cgarcia"
    usuario=request.session["usuario"]
    context = {'usuario':usuario}
    return render(request,'taller1/index.html', context)

def home(request):
    context = {}
    return render(request, 'taller1/home.html', context)


# Servicios 
def servicios(request):
    servicios = Servicio.objects.all()
    context = {"servicios": servicios}
    return render(request, 'taller1/catalogo.html', context)


def servicio_list(request):
    servicios = Servicio.objects.all()
    context = {"servicios": servicios}
    return render(request, 'taller1/servicio_list.html', context)



def servicio_add(request):
    mensaje = ""
    # Obtener el último `id_servicio` registrado y aumentar en 1
    ultimo_servicio = Servicio.objects.order_by('id_servicio').last()
    siguiente_id_servicio = int(ultimo_servicio.id_servicio) + 1 if ultimo_servicio else 1

    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "Servicio creado con éxito."
    else:
        form = ServicioForm(initial={'id_servicio': siguiente_id_servicio})

    return render(request, 'taller1/servicio_add.html', {'form': form, 'mensaje': mensaje})
    

def servicio_edit(request, pk):
    servicio = get_object_or_404(Servicio, id_servicio=pk)
    if request.method == "POST":
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            mensaje = "Bien, datos actualizados..."
            mensaje_tipo = "success"
        else:
            mensaje = "Error, datos no válidos."
            mensaje_tipo = "error"
        return render(request, 'taller1/servicio_edit.html', {'form': form, 'mensaje': mensaje, 'mensaje_tipo': mensaje_tipo})
    else:
        form = ServicioForm(instance=servicio)
        mensaje = ""
        mensaje_tipo = ""
    return render(request, 'taller1/servicio_edit.html', {'form': form, 'mensaje': mensaje, 'mensaje_tipo': mensaje_tipo})

def servicio_del(request, pk):
    try:
        # Obtén el objeto Servicio que deseas eliminar
        servicio = get_object_or_404(Servicio, id_servicio=pk)
        servicio.delete()  # Elimina el objeto

        # Mensaje de éxito
        messages.success(request, "Bien, servicio seleccionado eliminado...")
    except Servicio.DoesNotExist:
        # Mensaje de error si el servicio no existe
        messages.error(request, "Error, el servicio no existe...")

    # Redirige al usuario a la lista de servicios
    return redirect('servicio_list')


def mecanico_add(request):
    if request.method == "POST":
        form = MecanicoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'taller1/mecanico_add.html', {'form': form})  # Redirige a la página principal o a donde corresponda después de agregar el usuario
    else:
        form = MecanicoForm()

    return render(request, 'taller1/mecanico_add.html', {'form': form}) 


def mecanico_del(request, pk):
    try:
        # Obtén el objeto Servicio que deseas eliminar
        mecanico = get_object_or_404(Mecanico, rut=pk)
        mecanico.delete()  # Elimina el objeto

        # Mensaje de éxito
        messages.success(request, "Bien, el usuario seleccionado eliminado...")
    except Mecanico.DoesNotExist:
        # Mensaje de error si el servicio no existe
        messages.error(request, "Error, el usuario no existe...")

    # Redirige al usuario a la lista de servicios
    return redirect('crud')

def mecanico_edit(request, pk):
    mecanico = get_object_or_404(Mecanico, rut=pk)  # Utiliza get_object_or_404 para manejar usuarios no existentes
    if request.method == "POST":
        form = MecanicoForm(request.POST, instance=mecanico)
        if form.is_valid():  # Asegúrate de que el formulario es válido antes de guardar
            form.save()
            mensaje = "Bien, datos actualizados..."
            return redirect('mecanico_edit', pk=mecanico.rut)  # Redirige a una página de detalle o lista después de guardar
        else:
            mensaje = "Error, datos no válidos."
    else:
        form = MecanicoForm(instance=mecanico)
        mensaje = ""

    context = {'mecanico': mecanico, 'form': form, 'mensaje': mensaje}
    return render(request, 'taller1/mecanico_edit.html', context)