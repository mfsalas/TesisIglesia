# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movimiento_dinero', '0002_auto_20181108_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimiento_dinero',
            name='hora_movimiento',
        ),
        migrations.RemoveField(
            model_name='movimiento_dinero',
            name='motivo_movimiento',
        ),
    ]
