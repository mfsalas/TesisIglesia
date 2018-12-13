# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
        ('discipulado', '0006_auto_20181206_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discipulado',
            name='id_discipulador',
        ),
        migrations.RemoveField(
            model_name='discipulado',
            name='id_persona',
        ),
        migrations.RemoveField(
            model_name='discipulador',
            name='id_discipulador',
        ),
        migrations.AddField(
            model_name='discipulado',
            name='discipulador',
            field=models.ForeignKey(null=True, related_name='discipuladoDiscipulador', to='discipulado.Discipulador'),
        ),
        migrations.AddField(
            model_name='discipulado',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, related_name='discipuladopersona', to='persona.Persona'),
        ),
        migrations.AddField(
            model_name='discipulador',
            name='discipulador',
            field=models.CharField(max_length=50, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discipulador',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, related_name='persona', to='persona.Persona'),
        ),
    ]
