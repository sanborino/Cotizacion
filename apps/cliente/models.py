from django.db import models
from apps.tipoEvento.models import Evento

class Cliente(models.Model):
	nombre = models.CharField(max_length=100)
	telefono = models.CharField(max_length=10)
	celular = models.CharField(max_length=10)
	correo = models.CharField(max_length=50)
	alta = models.DateTimeField()
	evento = models.ForeignKey(Evento)

	def __unicode__(self):
		return self.nombre