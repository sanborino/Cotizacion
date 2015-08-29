
# -*- coding: utf-8 -*-
# from django.views.generic import CreateView
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from .models import Evento
# from django.core.urlresolvers import reverse_lazy

# class RegistrarEvento(CreateView):
# 	template_name = 'administracion/evento.html'
# 	model = Evento
# 	fields = '__all__'
# 	success_url = reverse_lazy('confirma')

# 	@method_decorator(login_required)
# 	def dispatch(self, *args, **kwargs):
# 		return super(RegistrarEvento, self).dispatch(*args, **kwargs)

from django.shortcuts import render_to_response
from forms import EventoForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import Evento

@login_required
def RegistrarEvento(request):
	if not request.user.is_staff:
		return HttpResponse("<h1>Acceso restringido consulte al administrador</h1>")

	eventos = Evento.objects.all()
	if request.method == 'POST':
		form = EventoForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/administracion/evento/')

	else:
		form = EventoForm()

	return render_to_response('administracion/evento.html',{'form':form, 'eventos': eventos},
		context_instance=RequestContext(request))