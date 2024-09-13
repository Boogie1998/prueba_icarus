from django.db import models

# Create your models here.

class Autor(models.Model):

    nombre = models.CharField("nombre completo del autor", max_length=30)
    fecha_nacimiento = models.DateField()

class Libros(models.Model):

    titulo = models.CharField("título del libro", max_length=50)
    autor = models.ForeignKey(Autor)
    fecha_pub = models.DateField()