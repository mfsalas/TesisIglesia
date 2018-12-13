# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
        ('discipulado', '0009_auto_20181206_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipulador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('discipulador', models.CharField(max_length=50)),
                ('persona', models.ForeignKey(blank=True, null=True, related_name='persona', to='persona.Persona')),
            ],
        ),
    ]
