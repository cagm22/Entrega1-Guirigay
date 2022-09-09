from django.db import models

# Create your models here.

class Cliente(models.Model):
    razon_social=models.CharField(max_length=40)
    domicilio=models.CharField(max_length=40)
#    localidad=models.CharField(max_length=40)
    dni_cuit=models.IntegerField()
    telefono=models.CharField(max_length=50)
#    correo=models.EmailField()

class Empleado(models.Model):
    nombre=models.CharField(max_length=40)

class Maquina(models.Model):
    marca:models.CharField(max_length=40)
    modelo:models.CharField(max_length=40)
    formato:models.CharField(max_length=40)
    sistema:models.CharField(max_length=40)
    contrasenia:models.CharField(max_length=40)
    falla:models.CharField(max_length=200)
    faltantes_tornillos:models.BooleanField()
    rayas_roturas:models.BooleanField()
    bateria:models.BooleanField()
    enciende:models.BooleanField()
    muestra_imagen:models.BooleanField()
    tiene_leds:models.BooleanField()
    cargador:models.BooleanField()
    backup:models.BooleanField()

