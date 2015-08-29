from django.conf.urls import include, url
from .views import Registrarse, Inicio

urlpatterns = [

url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'inicio/login.html'}, name = 'login' ),

url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name = 'logout' ),

url(r'^registrarse/$', Registrarse.as_view(), name = 'registrarse'),

url(r'^menu/$', Inicio.as_view(), name = 'menu'),

] 