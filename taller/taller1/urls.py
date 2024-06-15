#from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path ('', views.index, name='index'),
    path ('base', views.base, name='base'),
    path ('contacto', views.contacto, name='contacto'),
    path ('noticias', views.noticias, name='noticias'),
    path ('catalogo', views.catalogo, name='catalogo'),
    path ('carrito', views.carrito, name='carrito'),
    path('servicio1', views.servicio1, name='servicio1'),
    path('servicio2', views.servicio2, name='servicio2'),
    path('servicio3', views.servicio3, name='servicio3'),
    path('servicio4', views.servicio4, name='servicio4'),
    path('servicio5', views.servicio5, name='servicio5'),
    path('servicio6', views.servicio6, name='servicio6'),
    path('crud', views.crud, name='crud'),
    path('usuariosAdd', views.usuariosAdd, name='usuariosAdd'),
    
]