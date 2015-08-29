from django.conf.urls import include, url
from .views import RegistrarEstado, Confirmacion

urlpatterns = [

	url(r'^estado/$', RegistrarEstado.as_view(), name="estado"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),

]