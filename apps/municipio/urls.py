from django.conf.urls import include, url
from .views import RegistrarMunicipio
from apps.estado.views import Confirmacion

urlpatterns = [

	# url(r'^municipio/$', RegistrarMunicipio.as_view(), name="municipio"),
	url(r'^municipio/$', RegistrarMunicipio, name="municipio"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),
]