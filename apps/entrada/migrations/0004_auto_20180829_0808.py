# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0003_auto_20180829_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='fecha_entrada',
            field=models.DateField(blank=True),
        ),
    ]
