# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
        ('discipulado', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discipuladospersonas',
            name='id_discipulado',
        ),
        migrations.RemoveField(
            model_name='discipuladospersonas',
            name='id_discipulador',
        ),
        migrations.RemoveField(
            model_name='discipuladospersonas',
            name='id_persona',
        ),
        migrations.RenameField(
            model_name='discipulado',
            old_name='descripcion_discipulado',
            new_name='nombre_material_discipulado',
        ),
        migrations.AddField(
            model_name='discipulado',
            name='fecha_fin',
            field=models.CharField(max_length=10, default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discipulado',
            name='id_discipulador',
            field=models.ForeignKey(blank=True, null=True, to='discipulado.Discipulador'),
        ),
        migrations.AddField(
            model_name='discipulado',
            name='id_persona',
            field=models.ForeignKey(blank=True, null=True, to='persona.Persona'),
        ),
        migrations.DeleteModel(
            name='DiscipuladosPersonas',
        ),
    ]
