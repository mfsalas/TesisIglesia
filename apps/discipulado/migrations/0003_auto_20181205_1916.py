# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discipulado', '0002_auto_20181205_1816'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='discipulado',
            unique_together=set([('id_discipulador', 'id_persona')]),
        ),
    ]
