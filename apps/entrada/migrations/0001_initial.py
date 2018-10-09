# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '__first__'),
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cantidad_entrada', models.PositiveSmallIntegerField()),
                ('fecha_entrada', models.DateField()),
                ('observaciones_entrada', models.CharField(max_length=100)),
                ('id_articulo', models.ForeignKey(blank=True, null=True, to='inventario.Articulo')),
                ('id_ministerio', models.ForeignKey(blank=True, null=True, to='ministerio.Ministerios')),
            ],
        ),
    ]
