from django.db import models

from apps.persona.models import Persona
from apps.evento.models import Evento
from apps.persona.models import Matrimonio
from apps.ministerio.models import Ministerios


tipo_movimiento_choices = (
    ('IN', 'Ingreso'),
    ('EG', 'Egreso'),
)


#detalle_tipo_movimiento_ingresos_choices = (
#    ('Ingreso', (
#        ('Of', 'Ofrenda'),
#        ('Do', 'Donación'),
#        ('Ve', 'Venta'),
#        ('Di', 'Diezmo'),
#      )
#     ),
#     ('Egreso', (
#        ('Of', 'Ofrenda'),
#        ('Do', 'Donación'),
#        ('Gg', 'Gastos generales'),
#        ('Gm', 'Gastos ministeriales')
#      )
#    )
#)

#detalle_tipo_movimiento_egresos_choices = (
#    ('Of', 'Ofrenda'),
#    ('Do', 'Donación'),
#    ('Gg', 'Gastos generales'),
#    ('Gm', 'Gastos ministeriales'),
#)

clase_movimiento_choices = (
    ('FI', 'Fijo'),
    ('EV', 'Eventual'),
)


# Create your models here.
class Categoria(models.Model):
    tipo_movimiento = models.CharField(max_length=50, choices = tipo_movimiento_choices,null=False, blank=False) ##I/E
    nombre_categoria = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_categoria

class Movimiento_Dinero(models.Model):
    fecha_movimiento = models.CharField(max_length=10,null=False, blank=False)
    clase_movimiento = models.CharField(max_length=10, choices = clase_movimiento_choices)  ##F/E
    descripcion_movimiento = models.CharField(max_length=60, null=False, blank=False)
    monto_movimiento = models.CharField(max_length=10)
    id_categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    id_persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    id_evento = models.ForeignKey(Evento, null=True, blank=True, on_delete=models.CASCADE)
    id_matrimonio = models.ForeignKey(Matrimonio, null=True, blank=True, on_delete=models.CASCADE)
    id_ministerio = models.ForeignKey(Ministerios, null=True, blank=True, on_delete=models.CASCADE)
