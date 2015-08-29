from django.db import models

class Ingrediente(models.Model):
	nombre = models.CharField(max_length=50)
	medida = models.CharField(max_length=50)
	cantidad = models.DecimalField(max_digits=6, decimal_places=2)
	costo = models.DecimalField(max_digits=6, decimal_places=2)

	def __unicode__(self):
		return self.nombre