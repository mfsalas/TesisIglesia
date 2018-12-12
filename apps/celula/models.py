from django.db import models

# Create your models here.
class Celula(models.Model):
    dia_celula = models.CharField(max_length=10)
    hora_celula = models.TimeField()
    direccion_celula = models.CharField(max_length=50)
