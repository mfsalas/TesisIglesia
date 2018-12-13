# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discipulado', '0003_auto_20181205_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipulado',
            name='id_discipulador',
            field=models.ForeignKey(related_name='discipulador', to='discipulado.Discipulador'),
        ),
        migrations.AlterField(
            model_name='discipulado',
            name='id_persona',
            field=models.ForeignKey(default=4, related_name='persona', to='persona.Persona'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='discipulado',
            unique_together=set([]),
        ),
    ]
