from django.db import models


# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaEdicion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Item(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaEdicion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
