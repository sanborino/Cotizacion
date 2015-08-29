from django.db import models
from apps.cliente.models import Cliente
from apps.empresa.models import Empresa
from apps.receta.models import Receta

class Cotizacion(models.Model):
	empresa = models.ForeignKey(Empresa)
	fechaInicial = models.DateTimeField()
	fechaFinal = models.DateField()
	estado = models.CharField(max_length=20)
	personas = models.IntegerField(null=True)
	receta = models.ManyToManyField(Receta)
	venta = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	extra = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	descripcion = models.CharField(max_length=200, null=True)
	total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	cliente = models.ForeignKey(Cliente)

	def __unicode__(self):
		return "%s" % (self.estado)