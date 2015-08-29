# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import UserForm
from django.core.urlresolvers import reverse_lazy
from .models import Usuarios

class Registrarse(FormView):
	template_name = 'usuarios/capturaUsuarios.html'
	form_class = UserForm
	success_url = reverse_lazy('registrarse')

	def form_valid(self,form):
		user = form.save()
		perfil = Usuarios()
		perfil.usuario = user
		perfil.numeroUnico = form.cleaned_data['numeroUnico']
		perfil.save()
		return super(Registrarse,self).form_valid(form)

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(Registrarse, self).dispatch(*args, **kwargs)

class Inicio(TemplateView):
	template_name = 'inicio/menu.html'
	success_url = reverse_lazy('menu')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(Inicio, self).dispatch(*args, **kwargs)