# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingrediente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=10, decimal_places=2)),
                ('valor', models.DecimalField(max_digits=10, decimal_places=2)),
                ('estado', models.BooleanField()),
                ('item', models.ForeignKey(to='ingrediente.Ingrediente')),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
                ('creado', models.DateTimeField()),
                ('estado', models.BooleanField()),
                ('costo', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('venta', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='detalle',
            name='receta',
            field=models.ForeignKey(to='receta.Receta'),
        ),
    ]
