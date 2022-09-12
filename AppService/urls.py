from django.urls import path
from AppService.views import *

urlpatterns = [
    path('cliente/', cliente, name='Cliente'),
    path('', inicio, name='Inicio'),
    path('clientes/', clientes, name='Clientes'),
    path('clienteFormulario/', clienteFormulario, name='clienteFormulario'),
    path("maquinaFormulario/", maquinaFormulario, name='maquinaFormulario'),
    path("busquedaCliente/", busquedaCliente, name='busquedaCliente'),
    path("buscar/", buscar),
    #    path('urls/', funciones en views.py, name='url del padre.html'),


]
