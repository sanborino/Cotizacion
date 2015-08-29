from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('id','nombre', 'telefono','celular','correo','alta','evento')

admin.site.register(Cliente,ClienteAdmin)