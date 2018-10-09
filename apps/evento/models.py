from django.db import models

# Create your models here.
class Evento(models.Model):
    descripcion_evento = models.CharField(max_length=200)
    fecha_evento = models.CharField(max_length=10,null=False, blank=False)
    lugar_evento = models.CharField(max_length=30)
    hora_evento = models.CharField(max_length=5)

    def __str__(self):
        return '{} {}'.format(self.descripcion_evento,self.fecha_evento)
#    id_evento = models.ForeignKey(Ministerios, null=True, blank=True, on_delete=models.CASCADE) #es asi?
