from django.db import models


class Ministerios(models.Model):
    nombre_ministerio = models.CharField(max_length=50)
    dia_actividad = models.CharField(max_length=10)
    lugar_actividad = models.CharField(max_length=30)
    hora_actividad = models.CharField(max_length=5)
    fecha_baja_ministerio = models.DateField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre_ministerio
