from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base', views.base, name='base'),
    path('contacto', views.contacto, name='contacto'),
    path('noticias', views.noticias, name='noticias'),
    path('catalogo', views.servicios, name='catalogo'),  # Aquí mapea la URL /catalogo a la función servicios
    path('servicio', views.servicios, name='servicios'),
    path('servicio_list', views.servicio_list, name='servicio_list'),
    path('servicio_detalle', views.servicio_detalle, name='servicio_detalle'),
    path('servicio_add', views.servicio_add, name='servicio_add'),
    path('servicio_del/<str:pk>', views.servicio_del, name='servicio_del'),
    path('servicio_edit/<str:pk>', views.servicio_edit, name='servicio_edit'),
    path('carrito', views.carrito, name='carrito'),
    path('crud/', views.crud, name='crud'),
    path('UsuarioAdd', views.UsuarioAdd, name='UsuarioAdd'),
    path('Usuario_del/<str:pk>', views.Usuario_del, name='Usuario_del'),
    path('Usuario_edit/<str:pk>', views.Usuario_edit, name='Usuario_edit'),
    path('mecanico_add', views.mecanico_add, name='mecanico_add'),
    path('mecanico_del/<str:pk>', views.mecanico_del, name='mecanico_del'),
    path('mecanico_edit/<str:pk>', views.mecanico_edit, name='mecanico_edit'),
    path('home', views.home, name='home'),
]