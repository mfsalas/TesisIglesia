# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discipulado', '0004_auto_20181206_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipulado',
            name='id_discipulador',
            field=models.ForeignKey(null=True, related_name='discipulador', to='discipulado.Discipulador'),
        ),
        migrations.AlterField(
            model_name='discipulador',
            name='id_discipulador',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
