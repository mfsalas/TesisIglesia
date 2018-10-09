# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('descripcion_articulo', models.CharField(max_length=50)),
                ('cantidad_articulo', models.PositiveSmallIntegerField()),
                ('id_ministerio', models.ForeignKey(blank=True, null=True, to='ministerio.Ministerios')),
            ],
        ),
        migrations.CreateModel(
            name='Unidadad_de_Medida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre_unidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='id_unidad_de_medida',
            field=models.ForeignKey(blank=True, null=True, to='inventario.Unidadad_de_Medida'),
        ),
    ]
