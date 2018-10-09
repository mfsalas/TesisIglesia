# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_remove_articulo_id_ministerio'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='precio_Compra_articulo',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=2),
        ),
    ]
