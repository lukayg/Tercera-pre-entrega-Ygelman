from django.db import models

# Create your models here.

class Consola(models.Model):
    nombre = models.CharField(max_length=30)
    empresa = models.CharField(max_length=40)
    cantidad = models.IntegerField()

class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=30)
    empresa = models.CharField(max_length=30)
    cantidad = models.IntegerField()



