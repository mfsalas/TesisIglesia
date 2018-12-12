from django.db import models

# Create your models here.
class Matrimonio(models.Model):
    apellido_matrimonio = models.CharField(max_length=50)
    def __str__(self):
        return self.apellido_matrimonio

#rol para asignar a celulas y ministerios.
class Rol(models.Model):
    descripcion_rol = models.CharField(max_length=30)
    def __str__(self):
        return self.descripcion_rol


estado_civil_choices = (
    ('CA', 'Casado'),
    ('SO', 'Soltero'),
    ('VI', 'Viudo'),
    ('CO', 'Comprometido'),
    ('DI', 'Divorciado'),
)

si_no_choices = (
    ('SI', 'Sí'),
    ('NO', 'No'),
)

si_no_enCurso_choices = (
    ('SI', 'Sí'),
    ('NO', 'No'),
    ('EN CURSO', 'En curso'),
)

sexo_choices = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

class Persona(models.Model):
    nombre = models.CharField(max_length=50, blank=True)
    apellido_persona = models.CharField(max_length=50)
    fecha_nacimiento = models.CharField(max_length=10, null=False, blank=False)
    sexo = models.CharField(max_length=10, choices=sexo_choices,)
    celular = models.CharField(max_length=12)
    direccion = models.CharField(max_length=50)
    id_matrimonio = models.ForeignKey(Matrimonio, null=True, blank=True, on_delete=models.CASCADE)
    localidad = models.CharField(max_length=50)
    estado_civil = models.CharField(max_length=2, choices=estado_civil_choices,)
    profesion = models.CharField(max_length=35)
    bautizado = models.CharField(max_length=2, choices=si_no_choices,)
    escuela_biblica = models.CharField(max_length=2, choices=si_no_enCurso_choices,)
    encuentro = models.CharField(max_length=2, choices=si_no_choices,)

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellido_persona)
