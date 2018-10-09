from django.db import models

# Create your models here.
class Matrimonio(models.Model):
    apellido_matrimonio = models.CharField(max_length=50)
    def __str__(self):
        return self.apellido_matrimonio

class Persona(models.Model):
    nombre = models.CharField(max_length=50, blank=True)
    apellido_persona = models.CharField(max_length=50)
    fecha_nacimiento = models.CharField(max_length=10, null=False, blank=False)
    sexo = models.CharField(max_length=10)
    celular = models.CharField(max_length=12)
    direccion = models.CharField(max_length=50)
    id_matrimonio = models.ForeignKey(Matrimonio, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellido_persona)
