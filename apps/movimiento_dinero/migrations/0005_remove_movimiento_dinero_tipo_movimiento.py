# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movimiento_dinero', '0004_categoria_tipo_movimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimiento_dinero',
            name='tipo_movimiento',
        ),
    ]
