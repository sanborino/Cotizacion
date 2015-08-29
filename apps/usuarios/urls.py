from django.conf.urls import include, url
from .views import editar_perfil, perfil


urlpatterns = [
    url(r'^actualizado/$', perfil.as_view()),
    url(r'^perfil/$', editar_perfil),
    url(r'^password/$', 'django.contrib.auth.views.password_change', {'post_change_redirect' : '/actualizado/','template_name': 'usuarios/password.html'},),
]