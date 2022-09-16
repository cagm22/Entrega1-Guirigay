from django import forms


class MaquinaForm(forms.Form):
    marca=forms.CharField(max_length=40)
    modelo=forms.CharField(max_length=40)
    formato=forms.CharField(max_length=40)
    sistema=forms.CharField(max_length=40)
    contrasenia=forms.CharField(max_length=40)
    falla=forms.CharField(max_length=200)
    faltantes_tornillos=forms.BooleanField(required=False)
    rayas_roturas=forms.BooleanField(required=False)
    bateria=forms.BooleanField(required=False)
    enciende=forms.BooleanField(required=False)
    muestra_imagen=forms.BooleanField(required=False)
    tiene_leds=forms.BooleanField(required=False)
    cargador=forms.BooleanField(required=False)
    backup=forms.BooleanField(required=False) 

class EmpleadoForm(forms.Form):
    nombre=forms.CharField(max_length=40)
    dni_cuit=forms.IntegerField()
    telefono=forms.CharField(max_length=50)
    def __str__(self):
        return self.nombre