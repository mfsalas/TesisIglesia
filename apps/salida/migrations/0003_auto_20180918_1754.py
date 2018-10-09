# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salida', '0002_salida_fecha_salida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salida',
            name='fecha_salida',
            field=models.CharField(max_length=100),
        ),
    ]
