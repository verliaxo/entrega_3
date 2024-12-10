from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def lista_profes(request):
    p = Profesor.objects.all()  # ¡Falta el paréntesis en tu código!
    contexto = {
        'profesores': p
    }
    return render(request, 'app_1/lista_profes.html', contexto)

def lista_alumnos(request):
    a = Alumno.objects.all()  # ¡Falta el paréntesis en tu código!
    contexto = {
        'alumnos': a
    }
    return render(request, 'app_1/lista_alumnos.html', contexto)

def lista_entregas(request):
    e = Entrega.objects.all()  # ¡Falta el paréntesis en tu código!
    contexto = {
        'entregas': e
    }
    return render(request, 'app_1/lista_entregas.html', contexto)

def formulario_profes(request):
    if request.method == 'POST':  # Si se envió un formulario
        form = ProfesorFormulario(request.POST)  # Procesar los datos enviados
        if form.is_valid():  # Validar el formulario
            # Extraer los datos validados del formulario
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            edad = form.cleaned_data['edad']
            matricula = form.cleaned_data['matricula']
            materia = form.cleaned_data['materia']

            # Guardar los datos en la base de datos
            p = Profesor(nombre=nombre, apellido=apellido, edad=edad, matricula=matricula, materia=materia)
            p.save()
            
            # Redirigir a una página de éxito o mostrar un mensaje
            return lista_profes(request)
    else:  # Si no se envió nada (GET)
        form = ProfesorFormulario()  # Mostrar un formulario vacío

    return render(request, 'app_1/formulario_profes.html', {'form': form})

def formulario_alumnos(request):
    if request.method == 'POST':  # Si se envió un formulario
        form = AlumnoFormulario(request.POST)  # Procesar los datos enviados
        if form.is_valid():  # Validar el formulario
            # Extraer los datos validados del formulario
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            edad = form.cleaned_data['edad']
            matricula = form.cleaned_data['matricula']
            promedio = form.cleaned_data['promedio']

            # Guardar los datos en la base de datos
            a = Alumno(nombre=nombre, apellido=apellido, edad=edad, matricula=matricula, promedio=promedio)
            a.save()
            
            # Redirigir a una página de éxito o mostrar un mensaje
            return lista_alumnos(request)
    else:  # Si no se envió nada (GET)
        form = AlumnoFormulario()  # Mostrar un formulario vacío

    return render(request, 'app_1/formulario_alumnos.html', {'form': form})

def formulario_entregas(request):
    if request.method == 'POST':  # Si se envió un formulario
        form = EntregaFormulario(request.POST)  # Procesar los datos enviados
        if form.is_valid():  # Validar el formulario
            # Extraer los datos validados del formulario
            nombre = form.cleaned_data['nombre']
            fecha_de_entrega = form.cleaned_data['fecha_de_entrega']

            # Guardar los datos en la base de datos
            e = Entrega(nombre=nombre, fecha_de_entrega=fecha_de_entrega)
            e.save()
            
            # Redirigir a una página de éxito o mostrar un mensaje
            return lista_entregas(request)
    else:  # Si no se envió nada (GET)
        form = EntregaFormulario()  # Mostrar un formulario vacío

    return render(request, 'app_1/formulario_entregas.html', {'form': form})

def buscar_profe(request):
    buscar = None 
    form = BuscarProfe(request.POST or None)  

    if request.method == 'POST':
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            buscar = Profesor.objects.all()
            buscar = buscar.filter(nombre=nombre)
        
    return render(request, 'app_1/buscar_profe.html', {'form': form, 'resultados': buscar})
