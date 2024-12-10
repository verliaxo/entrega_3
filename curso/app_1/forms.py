from django import forms

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)  # Campo de texto con un máximo de 100 caracteres
    apellido = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    matricula = forms.IntegerField()
    materia = forms.CharField(max_length=20)

class BuscarProfe(forms.Form):
    nombre = forms.CharField(max_length=20)  # Campo de texto con un máximo de 100 caracteres

class AlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)  # Campo de texto con un máximo de 100 caracteres
    apellido = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    matricula = forms.IntegerField()
    promedio = forms.FloatField()

class EntregaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)  # Campo de texto con un máximo de 100 caracteres
    fecha_de_entrega = forms.DateField()


