from django.db import models

# Create your models here.

class Profesor(models.Model):
    nombre = models.CharField(max_length=20,blank=True)
    apellido = models.CharField(max_length=20,blank=True)
    edad = models.IntegerField(blank=True)
    matricula = models.IntegerField()
    materia = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.edad} - {self.matricula} - {self.materia}'

class Alumno(models.Model):
    nombre = models.CharField(max_length=20,blank=True)
    apellido = models.CharField(max_length=20,blank=True)
    edad = models.IntegerField(blank=True)
    matricula = models.IntegerField()
    promedio = models.FloatField()

    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.edad} - {self.matricula} - {self.promedio}'
    
class Entrega(models.Model):
    nombre = models.CharField(max_length=20,blank=True)
    fecha_de_entrega = models.DateField()

    def __str__(self):
        return f'{self.nombre} - {self.fecha_de_entrega}'