from django.db import models
from django.db.models import signals

from apps.ministerio.models import Ministerios
from apps.inventario.models import Articulo



class Entrada(models.Model):
    id_articulo = models.ForeignKey(Articulo, null=True, blank=True, on_delete=models.CASCADE)
    id_ministerio = models.ForeignKey(Ministerios, null=True, blank=True, on_delete=models.CASCADE)
    cantidad_entrada = models.PositiveSmallIntegerField()
    fecha_entrada = models.CharField(max_length=100,null=False, blank=False)
    observaciones_entrada = models.CharField(max_length=100)

def update_stock(sender, instance, **kwargs):
	instance.id_articulo.cantidad_articulo += instance.cantidad_entrada
	instance.id_articulo.save()

# register the signal
signals.post_save.connect(update_stock, sender=Entrada, dispatch_uid="update_stock_count")

def suma(self):
		return self.cantidad_entrada * self.id_articulo.precio_Compra_articulo
