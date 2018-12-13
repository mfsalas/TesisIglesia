# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '__first__'),
        ('evento', '0001_initial'),
        ('ministerio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre_categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento_Dinero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha_movimiento', models.CharField(max_length=10)),
                ('tipo_movimiento', models.CharField(max_length=50, choices=[('IN', 'Ingreso'), ('EG', 'Egreso')])),
                ('clase_movimiento', models.CharField(max_length=10, choices=[('FI', 'Fijo'), ('EV', 'Eventual')])),
                ('monto_movimiento', models.CharField(max_length=10)),
                ('descripcion_movimiento', models.CharField(max_length=50)),
                ('id_categoria', models.ForeignKey(blank=True, null=True, to='movimiento_dinero.Categoria')),
                ('id_evento', models.ForeignKey(blank=True, null=True, to='evento.Evento')),
                ('id_matrimonio', models.ForeignKey(blank=True, null=True, to='persona.Matrimonio')),
                ('id_ministerio', models.ForeignKey(blank=True, null=True, to='ministerio.Ministerios')),
                ('id_persona', models.ForeignKey(blank=True, null=True, to='persona.Persona')),
            ],
        ),
    ]
