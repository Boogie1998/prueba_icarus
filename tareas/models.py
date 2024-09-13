from django.db import models

# Create your models here.

class Tarea(models.Model):

    titulo = models.CharField("título de la tarea", max_length=30)
    descripcion = models.CharField("descripcion de la tarea", max_length=100)
    completada = models.BooleanField("estado de la tarea", default=False)