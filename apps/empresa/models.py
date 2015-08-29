from django.db import models
from apps.municipio.models import Municipio

class Empresa(models.Model):
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=200)
	telefono = models.CharField(max_length=10)
	celular = models.CharField(max_length=10)
	correo = models.CharField(max_length=50)
	contacto = models.CharField(max_length=50)
	municipio = models.ForeignKey(Municipio)

	def __unicode__(self):
		return self.nombre