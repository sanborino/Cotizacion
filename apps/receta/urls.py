from django.conf.urls import include, url
from .views import RegistrarReceta
from apps.estado.views import Confirmacion
from .views import ingredientes, editar, catalogoRecetas

urlpatterns = [

	url(r'^receta/$', RegistrarReceta, name="receta"),
	url(r'^ingredientes/$', ingredientes, name="ingredientes"),
	url(r'^editar/$', editar, name="editar"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),
	url(r'^catalogoR/$', catalogoRecetas, name="catalogoR"),
]