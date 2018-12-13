# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipulado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('descripcion_discipulado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Discipulador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_discipulador', models.CharField(max_length=10)),
                ('id_persona', models.ForeignKey(blank=True, null=True, to='persona.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='DiscipuladosPersonas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha_fin', models.CharField(max_length=10)),
                ('id_discipulado', models.ForeignKey(blank=True, null=True, to='discipulado.Discipulado')),
                ('id_discipulador', models.ForeignKey(blank=True, null=True, to='discipulado.Discipulador')),
                ('id_persona', models.ForeignKey(blank=True, null=True, to='persona.Persona')),
            ],
        ),
    ]
