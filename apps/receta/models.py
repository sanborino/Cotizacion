from django.db import models
from apps.ingrediente.models import Ingrediente


class Receta(models.Model):
	nombre = models.CharField(max_length=250)
	creado = models.DateTimeField()
	estado = models.BooleanField()
	costo = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	venta = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	# class Meta:
	# 	get_latest_by = 'creado'

	def __unicode__(self):
		return self.nombre

class Detalle(models.Model):
	receta = models.ForeignKey(Receta)
	item = models.ForeignKey(Ingrediente)
	cantidad = models.DecimalField(max_digits=10, decimal_places=2)
	valor = models.DecimalField(max_digits=10, decimal_places=2)
	estado = models.BooleanField()

	def __unicode__(self):
		return "%s" % (self.estado)