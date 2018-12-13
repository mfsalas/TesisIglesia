# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movimiento_dinero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimiento_dinero',
            name='hora_movimiento',
            field=models.CharField(max_length=10, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movimiento_dinero',
            name='motivo_movimiento',
            field=models.CharField(max_length=50, blank=True, null=True, choices=[('Of', 'Ofrenda'), ('Do', 'Donación'), ('Ve', 'Venta'), ('Di', 'Diezmo')]),
        ),
        migrations.AlterField(
            model_name='movimiento_dinero',
            name='descripcion_movimiento',
            field=models.CharField(max_length=60),
        ),
    ]
