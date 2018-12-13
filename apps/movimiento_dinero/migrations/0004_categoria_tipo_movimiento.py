# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movimiento_dinero', '0003_auto_20181108_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='tipo_movimiento',
            field=models.CharField(max_length=50, default=2, choices=[('IN', 'Ingreso'), ('EG', 'Egreso')]),
            preserve_default=False,
        ),
    ]
