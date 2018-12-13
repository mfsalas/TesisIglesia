from django.db import models

# Create your models here.
from apps.persona.models import Persona

class Discipulador(models.Model):
    discipulador = models.CharField(max_length=50)#ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    persona =models.ForeignKey(Persona, null=True, blank=True, related_name="persona", on_delete=models.CASCADE)

    def __str__(self):
        return self.id_discipulador

class Discipulado(models.Model):
    nombre_material_discipulado = models.CharField(max_length=50)
    discipulador = models.ForeignKey(Persona, null=True, blank=False, related_name="discipuladoDiscipulador", on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, null=True, blank=True, related_name="discipuladopersona", on_delete=models.CASCADE)
    fecha_fin = models.CharField(max_length=10,null=False, blank=False)

    def __str__(self):
        return self.id_persona
