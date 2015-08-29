from django.db import models
from apps.estado.models import Estado

class Municipio(models.Model):
	nombre = models.CharField(max_length=50)
	estado = models.ForeignKey(Estado)

	def __unicode__(self):
		return self.nombre