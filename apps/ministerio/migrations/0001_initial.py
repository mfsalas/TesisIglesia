# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ministerios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre_ministerio', models.CharField(max_length=50)),
                ('dia_actividad', models.CharField(max_length=10)),
                ('lugar_actividad', models.CharField(max_length=30)),
                ('hora_actividad', models.CharField(max_length=5)),
                ('encargado_ministerio', models.ForeignKey(blank=True, null=True, to='persona.Persona')),
            ],
        ),
    ]
