# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discipulado', '0007_auto_20181206_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discipulador',
            name='persona',
        ),
        migrations.AlterField(
            model_name='discipulado',
            name='discipulador',
            field=models.ForeignKey(null=True, related_name='discipuladoDiscipulador', to='persona.Persona'),
        ),
        migrations.DeleteModel(
            name='Discipulador',
        ),
    ]
