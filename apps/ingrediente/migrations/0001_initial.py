# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('medida', models.CharField(max_length=50)),
                ('cantidad', models.DecimalField(max_digits=6, decimal_places=2)),
                ('costo', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
        ),
    ]
