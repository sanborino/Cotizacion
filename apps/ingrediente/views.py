# -*- coding: utf-8 -*-
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Ingrediente
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Ingrediente
from django.http import HttpResponse

class RegistrarIngrediente(CreateView):
	template_name = 'administracion/ingrediente.html'
	model = Ingrediente
	fields = '__all__'
	success_url = reverse_lazy('ingrediente')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(RegistrarIngrediente, self).dispatch(*args, **kwargs)

@login_required
def catalogoProductos(request):
	if not request.user.is_staff:
		return HttpResponse("<h1>Acceso restringido consulte al administrador</h1>")

	articulo = Ingrediente.objects.all()

	ctx = {'articulo':articulo}
	return render_to_response('administracion/catalogoI.html',ctx,context_instance=RequestContext(request))
