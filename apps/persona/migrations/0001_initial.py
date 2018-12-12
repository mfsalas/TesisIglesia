# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matrimonio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('apellido_matrimonio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('apellido_persona', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.CharField(max_length=10)),
                ('sexo', models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino')])),
                ('celular', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=50)),
                ('localidad', models.CharField(max_length=50)),
                ('estado_civil', models.CharField(max_length=2, choices=[('CA', 'Casado'), ('SO', 'Soltero'), ('VI', 'Viudo'), ('CO', 'Comprometido'), ('DI', 'Divorciado')])),
                ('profesion', models.CharField(max_length=35)),
                ('bautizado', models.CharField(max_length=2, choices=[('SI', 'Sí'), ('NO', 'No')])),
                ('escuela_biblica', models.CharField(max_length=2, choices=[('SI', 'Sí'), ('NO', 'No'), ('EN CURSO', 'En curso')])),
                ('encuentro', models.CharField(max_length=2, choices=[('SI', 'Sí'), ('NO', 'No')])),
                ('id_matrimonio', models.ForeignKey(blank=True, null=True, to='persona.Matrimonio')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('descripcion_rol', models.CharField(max_length=30)),
            ],
        ),
    ]
