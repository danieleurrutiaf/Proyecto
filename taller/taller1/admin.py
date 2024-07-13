from django.contrib import admin
from django.contrib import admin
from .models import Genero, Usuario, Servicio,Mecanico
# Register your models here.
admin.site.register(Genero)
admin.site.register(Usuario)
admin.site.register(Servicio)
admin.site.register(Mecanico)