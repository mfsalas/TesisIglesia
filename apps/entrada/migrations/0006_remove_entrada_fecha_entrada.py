# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0005_auto_20180829_0809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='fecha_entrada',
        ),
    ]
