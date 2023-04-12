from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()
    carrera = models.CharField(max_length=16)

class Asignatura(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.IntegerField()

class Docente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()
