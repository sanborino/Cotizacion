from django.contrib import admin
from .models import Cotizacion

class CotizacionAdmin(admin.ModelAdmin):
	list_display = ('id','empresa', 'cliente','estado','total')

admin.site.register(Cotizacion,CotizacionAdmin)