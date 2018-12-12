# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discipulado', '0008_auto_20181206_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipulado',
            name='discipulador',
            field=models.CharField(max_length=50, default=1),
            preserve_default=False,
        ),
    ]
