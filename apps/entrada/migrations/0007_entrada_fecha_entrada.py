# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0006_remove_entrada_fecha_entrada'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='fecha_entrada',
            field=models.DateField(default=datetime.datetime(2018, 8, 29, 11, 47, 8, 714609, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
