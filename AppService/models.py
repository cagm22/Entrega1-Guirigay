from email.policy import default
from django.db import models

# Create your models here.

class Cliente(models.Model):
    razon_social=models.CharField(max_length=40)
    domicilio=models.CharField(max_length=40)
#    localidad=models.CharField(max_length=40)
    dni_cuit=models.IntegerField()
    telefono=models.CharField(max_length=50)
#    correo=models.EmailField()
    def __str__(self):
        return self.razon_social#" "+str(self.apellido) # eeste ej es para el modelo Estudiante

class Empleado(models.Model):
    nombre=models.CharField(max_length=40)
    dni_cuit=models.IntegerField(default=0)
    telefono=models.CharField(max_length=50, default=0)
    def __str__(self):
        return self.nombre

class Maquina(models.Model):
    marca=models.CharField(max_length=40, default="/")
    modelo=models.CharField(max_length=40, default="/")
    formato=models.CharField(max_length=40, default="/")
    sistema=models.CharField(max_length=40, default="/")
    contrasenia=models.CharField(max_length=40, default="/")
    falla=models.CharField(max_length=200, default="/")
    faltantes_tornillos=models.BooleanField(default=False,blank=True)
    rayas_roturas=models.BooleanField(default=False,blank=True)
    bateria=models.BooleanField(default=False,blank=True)
    enciende=models.BooleanField(default=False,blank=True)
    muestra_imagen=models.BooleanField(default=False,blank=True)
    tiene_leds=models.BooleanField(default=False,blank=True)
    cargador=models.BooleanField(default=False,blank=True)
    backup=models.BooleanField(default=False,blank=True)
    def __str__(self):
        return self.marca+ " " +str(self.modelo)