# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tipoEvento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
                ('celular', models.CharField(max_length=10)),
                ('correo', models.CharField(max_length=50)),
                ('alta', models.DateTimeField()),
                ('evento', models.ForeignKey(to='tipoEvento.Evento')),
            ],
        ),
    ]
