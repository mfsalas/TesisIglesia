# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0002_auto_20180829_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='fecha_entrada',
            field=models.DateField(),
        ),
    ]
