from django.db import models

from apps.persona.models import Persona ###

# Create your models here.
class Celula(models.Model):
    dia_celula = models.CharField(max_length=10)
    hora_celula = models.TimeField()
    direccion_celula = models.CharField(max_length=50)
    encargado_celula = models.ForeignKey(Persona, null=True, blank=True)
    def __str__(self):                      #no se si hace falta esto
        return self.dia_celula

class Miembros_celula(models.Model):
    encargado_celula = models.ForeignKey(Celula, null=True, blank=True, on_delete=models.CASCADE)
    miembro = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
#    rol = models.CharField(max_length=10)
    def __str__(self):
        return self.miembro
