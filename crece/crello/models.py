from django.db import models

# Create your models here.
class Tablero(models.Model):
    nombre = models.CharField(max_length=60,verbose_name='NOMBRE')
    
class Lista(models.Model):
    nombre = models.CharField(max_length=60,verbose_name='NOMBRE')
    fk_Tablero = models.ForeignKey(Tablero, on_delete = models.CASCADE)

class Tarjeta(models.Model):
    nombre = models.CharField(max_length=60,verbose_name='NOMBRE')
    descripcion = models.CharField(max_length=250,verbose_name='DESCRIPCIÓN')
    fk_Lista = models.ForeignKey(Lista, on_delete = models.CASCADE,related_name='tarjetas')
        