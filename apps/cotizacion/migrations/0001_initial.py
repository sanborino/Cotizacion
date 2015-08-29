# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
        ('cliente', '0001_initial'),
        ('receta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaInicial', models.DateTimeField()),
                ('fechaFinal', models.DateField()),
                ('estado', models.CharField(max_length=20)),
                ('personas', models.IntegerField(null=True)),
                ('venta', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('extra', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('descripcion', models.CharField(max_length=200, null=True)),
                ('total', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('cliente', models.ForeignKey(to='cliente.Cliente')),
                ('empresa', models.ForeignKey(to='empresa.Empresa')),
                ('receta', models.ManyToManyField(to='receta.Receta')),
            ],
        ),
    ]
