# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discipulado', '0010_discipulador'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discipulado',
            old_name='discipulador',
            new_name='id_discipulador',
        ),
        migrations.RenameField(
            model_name='discipulado',
            old_name='persona',
            new_name='id_persona',
        ),
        migrations.RenameField(
            model_name='discipulador',
            old_name='discipulador',
            new_name='id_discipulador',
        ),
        migrations.RenameField(
            model_name='discipulador',
            old_name='persona',
            new_name='id_persona',
        ),
    ]
