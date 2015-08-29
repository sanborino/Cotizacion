from django.db import models

class Estado(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre