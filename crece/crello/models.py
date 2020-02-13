from django.db import models

# Create your models here.
class Tablero(models.Model):
    nombre = models.CharField(max_length=60)
    
class Lista(models.Model):
    nombre = models.CharField(max_length=60)
    fk_Tablero = models.ForeignKey(Tablero, on_delete = models.CASCADE)

class Tarjeta(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=250)
    fk_Lista = models.ForeignKey(Lista, on_delete = models.CASCADE)
        