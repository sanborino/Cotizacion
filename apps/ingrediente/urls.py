from django.conf.urls import include, url
from .views import RegistrarIngrediente, catalogoProductos
from apps.estado.views import Confirmacion

urlpatterns = [

	url(r'^ingrediente/$', RegistrarIngrediente.as_view(), name="ingrediente"),
	url(r'^catalogoI/$', catalogoProductos, name="catalogoI"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),

]