from django.db import models

from apps.persona.models import Persona ###

class Ministerios(models.Model):
    nombre_ministerio = models.CharField(max_length=50)
    dia_actividad = models.CharField(max_length=10)
    lugar_actividad = models.CharField(max_length=30)
    hora_actividad = models.CharField(max_length=5)
    encargado_ministerio = models.ForeignKey(Persona, null=True, blank=True)

    def __str__(self):
        return self.nombre_ministerio
