from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('estudiantes/', estudiantes),
    path('docentes/', docentes),
    path('asignaturas/', asignaturas),
    path('agregar_estudiante/', agregarEstudiante),
    path('agregar_docente/', agregarDocente),
    path('agregar_asignatura/', agregarAsignatura),
    path('docente/', docente),
    path('estudiante/', estudiante),
    path('asignatura/', asignatura)
]