from django.shortcuts import render, redirect
from django.http import HttpResponse
from Uniapp.models import Estudiante, Docente, Asignatura
# Create your views here.

def index(request):
    return render(request, 'index.html')

def docentes(request):
    docentes = Docente.objects.all()
    return render(request, "docentes.html", {"docentes": docentes})

def agregarDocente(request):
    nombres = request.POST['nombres']
    apellidos = request.POST['apellidos']
    edad = request.POST['edad']
    email = request.POST['email']
    Docente.objects.create(nombres=nombres, apellidos=apellidos, edad=edad, email=email)
    return redirect("/docentes/")

def docente(request):
    docente = None
    campo = request.POST['campo']
    try:
        campo = int(campo)
        docente = Docente.objects.get(id=campo)
    except:
        docente = Docente.objects.filter(apellidos__icontains=campo).first()
    
    if docente != None:
        return render(request, "docente.html", {"docente": docente})
    else:
        return redirect('/docentes/')

def estudiante(request):
    estudiante = None
    campo = request.POST['campo']
    try:
        campo = int(campo)
        estudiante = Estudiante.objects.get(id=campo)
    except:
        estudiante = Estudiante.objects.filter(apellidos__icontains=campo).first()
    
    if estudiante != None:
        return render(request, "estudiante.html", {"estudiante": estudiante})
    else:
        return redirect('/docentes/')

def asignatura(request):
    asignatura = None
    campo = request.POST['campo']
    try:
        campo = int(campo)
        asignatura = Asignatura.objects.get(id=campo)
    except:
        asignatura = Asignatura.objects.filter(nombre__icontains=campo).first()
    
    if asignatura != None:
        return render(request, "asignatura.html", {"asignatura": asignatura})
    else:
        return redirect('/asignaturas/')

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "estudiantes.html", {"estudiantes": estudiantes})

def agregarEstudiante(request):
    nombres = request.POST['nombres']
    apellidos = request.POST['apellidos']
    edad = request.POST['edad']
    email = request.POST['email']
    carrera = request.POST['carrera']
    Estudiante.objects.create(nombres=nombres, apellidos=apellidos, edad=edad, email=email, carrera=carrera)
    return redirect("/estudiantes/")

def asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, "asignaturas.html", {"asignaturas": asignaturas})

def agregarAsignatura(request):
    nombre = request.POST['nombre']
    creditos = request.POST['creditos']
    Asignatura.objects.create(nombre=nombre, creditos=creditos)
    return redirect("/asignaturas/")
