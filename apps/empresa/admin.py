from django.contrib import admin
from .models import Empresa

class EmpresaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre', 'direccion','telefono','correo')

admin.site.register(Empresa, EmpresaAdmin)