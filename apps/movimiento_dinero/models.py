from django.db import models

from apps.persona.models import Persona
from apps.evento.models import Evento
from apps.persona.models import Matrimonio
from apps.ministerio.models import Ministerios

# Create your models here.
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_categoria

class Movimiento_Dinero(models.Model):
    fecha_movimiento = models.CharField(max_length=10,null=False, blank=False)
    tipo_movimiento = models.CharField(max_length=50)
    clase_movimiento = models.CharField(max_length=10)
    monto_movimiento = models.CharField(max_length=10)
    id_categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    descripcion_movimiento = models.CharField(max_length=50)
    id_persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    id_evento = models.ForeignKey(Evento, null=True, blank=True, on_delete=models.CASCADE)
    id_matrimonio = models.ForeignKey(Matrimonio, null=True, blank=True, on_delete=models.CASCADE)
    id_ministerio = models.ForeignKey(Ministerios, null=True, blank=True, on_delete=models.CASCADE)
    fecha_baja_movimiento_dinero = models.DateField(max_length=50, blank=True, null=True)
