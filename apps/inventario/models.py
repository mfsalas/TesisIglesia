from django.db import models
import decimal



class Unidadad_de_Medida(models.Model):
    nombre_unidad = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_unidad

class Articulo(models.Model):
    descripcion_articulo = models.CharField(max_length=50)
    cantidad_articulo = models.PositiveSmallIntegerField()
    id_unidad_de_medida = models.ForeignKey(Unidadad_de_Medida, null=True, blank=True, on_delete=models.CASCADE)
    precio_Compra_articulo = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.descripcion_articulo

def preeciototal(self):
	precio_total=self.precio_Compra_articulo*self.cantidad_articulo
	return precio_total
