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
    path ('proyecto1', views.proyecto1, name='proyecto1'),
    
]