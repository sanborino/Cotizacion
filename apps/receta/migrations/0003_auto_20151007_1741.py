# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0002_auto_20151007_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='cantidad',
            field=models.DecimalField(max_digits=15, decimal_places=2),
        ),
    ]
