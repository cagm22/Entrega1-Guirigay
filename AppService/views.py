from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppService.forms import MaquinaForm , EmpleadoForm
# Create your views here.

def cliente(request):
    cliente=Cliente(razon_social="carlos biribay" , domicilio="ciudad de la paz 1500 caba" , dni_cuit=95252551 , telefono="1551313161")
    cliente.save()
    texto=f"cliente creado de nombre: {cliente.razon_social} y telefono {cliente.telefono}"
    return HttpResponse(texto)

#def inicio(request):
#    texto="Pagina de Inicio"
#    return HttpResponse(texto)

def inicio(request):
    return render(request, "AppService/inicio.html") 

def clientes(request):
    return render(request, "AppService/clientes.html")

def clienteFormulario(request):
    if request.method == "POST":
        razon_social = request.POST["razon_social"]
        dni_cuit = request.POST["dni_cuit"]
        domicilio = request.POST["domicilio"]
        telefono = request.POST["telefono"]
        cliente=Cliente(razon_social=razon_social, dni_cuit=dni_cuit,domicilio=domicilio,telefono=telefono)
        cliente.save()
        return render(request, "AppService/inicio.html")

    return render(request, "AppService/clienteFormulario.html")


def maquinaFormulario(request):
    if request.method == "POST":
        print("VINO POR POST")
        form= MaquinaForm(request.POST)
        print(form)
        if form.is_valid():
            info=form.cleaned_data
            marca=info["marca"]
            modelo=info["modelo"]
            formato=info["formato"]
            sistema=info["sistema"]
            contrasenia=info["contrasenia"]
            falla=info["falla"]
            faltantes_tornillos=info["faltantes_tornillos"]
            rayas_roturas=info["rayas_roturas"]
            bateria=info["bateria"]
            enciende=info["enciende"]
            muestra_imagen=info["muestra_imagen"]
            tiene_leds=info["tiene_leds"]
            cargador=info["cargador"]
            backup=info["backup"]
            maquina=Maquina(marca=marca,modelo=modelo,formato=formato,
            sistema=sistema,contrasenia=contrasenia,falla=falla,
            faltantes_tornillos=faltantes_tornillos,rayas_roturas=rayas_roturas,
            bateria=bateria,enciende=enciende,muestra_imagen=muestra_imagen,
            tiene_leds=tiene_leds,cargador=cargador,backup=backup)
            maquina.save()
            return render(request, "AppService/inicio.html", {"mensaje": "Maquina creada"})

    else: 
        print("vino por get")
        form=MaquinaForm()
        return render(request, "AppService/maquinaFormulario.html" , {"form":form})


def empleadoFormulario(request):
    if request.method == "POST":
        print("Vino por post")
        form= EmpleadoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            dni_cuit=info["dni_cuit"]
            telefono=info["telefono"]
            empleado=Empleado(nombre=nombre,dni_cuit=dni_cuit,telefono=telefono)
            empleado.save()
            return render(request, "AppService/inicio.html", {"mensaje": "Empleado ha sido creado"})
    else: 
        print("vino por get")
        form=EmpleadoForm()
        return render(request, "AppService/empleadoFormulario.html" , {"form":form})

def busquedaTelefono(request):
    return render(request, "AppService/busquedaTelefono.html")

def buscar(request):
    if request.GET["telefono"]:
        telefono=request.GET["telefono"]
        clientes=Cliente.objects.filter(telefono=telefono)
        #clientes=Cliente.objects.filter(telefono__icontains=telefono) # nos muestra resultados que contengan
        #clientes=Cliente.objects.all() # nos muestra todos los objetos de clientes
        return render(request, "AppService/resultadosBusqueda.html", {"clientes":clientes})
    else:
        return render(request, "AppService/busquedaTelefono.html", {"mensaje":"ingrese un telefono valido"})
