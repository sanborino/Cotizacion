# -*- coding: utf-8 -*-
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Estado
from django.core.urlresolvers import reverse_lazy

from django.http import HttpResponse

class RegistrarEstado(CreateView):

	template_name = 'localidad/estado.html'
	model = Estado
	fields = '__all__'
	success_url = reverse_lazy('confirma')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(RegistrarEstado, self).dispatch(*args, **kwargs)

class Confirmacion(TemplateView):
    template_name = 'inicio/confirma.html'
    success_url = reverse_lazy('confirma')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
    	return super(Confirmacion, self).dispatch(*args, **kwargs)

    

