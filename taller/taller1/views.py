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
    context = {"Usuarios": usuarios}
    return render(request, 'taller1/usuarios_list.html', context)


def UsuarioAdd(request):
    if request.method is "POST":
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        activo="1"


        objGenero=Genero.objects.get(id_genero = genero)
        obj=Usuario.objects.create( rut=rut,
                                    nombre=nombre,
                                    apellido_paterno=aPaterno,
                                    apellido_materno=aMaterno,
                                    fecha_nacimiento=fechaNac,
                                    id_genero=objGenero,
                                    telefono=telefono,
                                    email=email,
                                    activo=1 )
        
        obj.save()
        context={'mensaje' : "OK, datos grabados..."}
        return render(request, 'taller1/usuarios_add.html', context) 
    else:
        generos=Genero.objects.all()
        context= {'generos': generos}
        return render(request, 'taller1/usuarios_add.html', context)
    

def Usuario_del(request, pk):
    context={}
    try:

        usuario=Usuario.objects.get(rut=pk)

        usuario.delete()
        mensaje="Bien, datos eliminados"
        usuario= Usuario.objects.all()
        context= {'usuario': usuario, 'mensaje': mensaje}
        return render(request, 'taller1/usuario_list.html', context)
    
    except:
        mensaje="Error, rut no existe..."
        usuario= Usuario.objects.all()
        context= {'usuario': usuario, 'mensaje': mensaje}
        return render(request, 'taller1/usuarios_list.html', context)


def Usuario_findEdit (request,pk):

    if pk != "":
        usuario= Usuario.objects.get(rut=pk)
        generos=Genero.objects.all()

        print(type(usuario.id_genero.genero))

        context={'usuario': usuario, 'generos': generos}
        if usuario:
            return render (request, 'taller1/usuarios_edit.html', context)
        else:
            context={'mensaje': "Error, rut no existe..." }
            return render(request, 'taller1/usuarios_list.html', context)



def UsuarioUpdate (request):

    if request.method != "POST":

        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        activo="1"

        objGenero=Genero.objects.get(id_genero = genero)

        usuario = Usuario()
        usuario.rut=rut,
        usuario.nombre=nombre,
        usuario.apellido_paterno=aPaterno,
        usuario.apellido_materno=aMaterno,
        usuario.fecha_nacimiento=fechaNac,
        usuario.id_genero=objGenero,
        usuario.telefono=telefono,
        usuario.email=email,
        usuario.activo=1
        usuario.save()

        generos=Genero.objects.all()
        context={'mensaje': "OK, datos actualizados...", 'generos': generos, 'usuario':usuario}
        return render(request, 'taller1/usuarios_edir.html', context)
    
    else:
        usuarios= Usuario.objects.all()
        context={'usuarios': usuarios}
        return render(request, 'taller1/usuarios_list.html', context)









    

