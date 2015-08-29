from django.contrib import admin
from .models import Municipio

class MunicipioAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','estado')

admin.site.register(Municipio,MunicipioAdmin)