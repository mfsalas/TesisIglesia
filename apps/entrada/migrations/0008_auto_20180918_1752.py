# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0007_entrada_fecha_entrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='fecha_entrada',
            field=models.CharField(max_length=100),
        ),
    ]
