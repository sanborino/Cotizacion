from django.conf.urls import include, url
from .views import RegistrarCliente, clientesTodos
from apps.estado.views import Confirmacion

urlpatterns = [

	url(r'^cliente/$', RegistrarCliente, name="cliente"),
	url(r'^clientes/$', clientesTodos, name="clientes"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),
]