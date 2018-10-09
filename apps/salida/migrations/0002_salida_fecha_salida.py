# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('salida', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salida',
            name='fecha_salida',
            field=models.DateField(default=datetime.datetime(2018, 8, 29, 23, 52, 18, 841446, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
