# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discipulado', '0005_auto_20181206_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discipulador',
            name='id_persona',
        ),
        migrations.AlterField(
            model_name='discipulador',
            name='id_discipulador',
            field=models.ForeignKey(default=5, to='persona.Persona'),
            preserve_default=False,
        ),
    ]
