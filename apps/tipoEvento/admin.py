from django.contrib import admin
from .models import Evento

class EventoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

admin.site.register(Evento,EventoAdmin)