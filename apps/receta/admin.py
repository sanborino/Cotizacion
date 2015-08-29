from django.contrib import admin
from .models import Receta, Detalle

class RecetaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre', 'estado')


class DetalleAdmin(admin.ModelAdmin):
	list_display = ('id','receta', 'item','cantidad','valor')
	list_filter = ('receta',)

admin.site.register(Receta,RecetaAdmin)
admin.site.register(Detalle,DetalleAdmin)