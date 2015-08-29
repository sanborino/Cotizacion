from django.contrib import admin
from .models import Usuarios

class UsuariosAdmin(admin.ModelAdmin):
	list_display = ('id','usuario', 'numeroUnico')

admin.site.register(Usuarios,UsuariosAdmin)