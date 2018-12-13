# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('dia_celula', models.CharField(max_length=10)),
                ('hora_celula', models.TimeField()),
                ('direccion_celula', models.CharField(max_length=50)),
                ('encargado_celula', models.ForeignKey(blank=True, null=True, to='persona.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Miembros_celula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('rol', models.CharField(max_length=10)),
                ('encargado_celula', models.ForeignKey(blank=True, null=True, to='celula.Celula')),
                ('miembro', models.ForeignKey(blank=True, null=True, to='persona.Persona')),
            ],
        ),
    ]
