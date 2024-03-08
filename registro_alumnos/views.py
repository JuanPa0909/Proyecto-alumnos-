from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Alumno
from .forms import AlumnoForm
from datetime import date

def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'listar_alumnos.html', {'alumnos': alumnos})

def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'agregar_alumno.html', {'form': form})

def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'editar_alumno.html', {'form': form})

def eliminar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    return redirect('listar_alumnos')


# Definir función para calcular la edad
def calcular_edad(fecha_nacimiento):
    today = date.today()
    age = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return age

def estadisticas_alumnos(request):
    # Obtener todos los alumnos
    alumnos = Alumno.objects.all()

    # Calcular la edad de cada alumno y almacenarla en una lista
    edades = [calcular_edad(alumno.fecha_nacimiento) for alumno in alumnos]

    # Calcular el conteo de cada edad
    conteo_edades = {}
    for edad in edades:
        if edad in conteo_edades:
            conteo_edades[edad] += 1
        else:
            conteo_edades[edad] = 1

    return render(request, 'estadisticas_alumnos.html', {'conteo_edades': conteo_edades})
