from django.contrib import admin
from .models import Ingrediente

class IngredienteAdmin(admin.ModelAdmin):
	list_display = ('id','nombre', 'medida','cantidad','costo')

admin.site.register(Ingrediente,IngredienteAdmin)