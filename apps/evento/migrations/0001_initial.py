# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('descripcion_evento', models.CharField(max_length=200)),
                ('fecha_evento', models.CharField(max_length=10)),
                ('lugar_evento', models.CharField(max_length=30)),
                ('hora_evento', models.CharField(max_length=5)),
            ],
        ),
    ]
