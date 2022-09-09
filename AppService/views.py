from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def cliente(request):
    cliente=Cliente(razon_social="carlos biribay" , domicilio="ciudad de la paz 1500 caba" , dni_cuit=95252551 , telefono="1551313161")
    cliente.save()
    texto=f"cliente creado de nombre: {cliente.razon_social} y telefono {cliente.telefono}"
    return HttpResponse(texto)