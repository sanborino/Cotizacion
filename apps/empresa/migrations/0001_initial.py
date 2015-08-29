# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('municipio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=10)),
                ('celular', models.CharField(max_length=10)),
                ('correo', models.CharField(max_length=50)),
                ('contacto', models.CharField(max_length=50)),
                ('municipio', models.ForeignKey(to='municipio.Municipio')),
            ],
        ),
    ]
