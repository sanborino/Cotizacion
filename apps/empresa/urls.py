from django.conf.urls import include, url
from .views import RegistrarEmpresa
from apps.estado.views import Confirmacion

urlpatterns = [

	url(r'^empresa/$', RegistrarEmpresa, name="empresa"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),
]