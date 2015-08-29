from django.conf.urls import include, url
from .views import RegistrarEvento
from apps.estado.views import Confirmacion

urlpatterns = [

	url(r'^evento/$', RegistrarEvento, name="evento"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),

]