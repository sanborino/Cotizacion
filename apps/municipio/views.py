# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from forms import MunicipioForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponse

@login_required
def RegistrarMunicipio(request):
	if not request.user.is_staff:
		return HttpResponse("<h1>Acceso restringido consulte al administrador</h1>")
	if request.method == 'POST':
		form = MunicipioForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/localidad/confirma/')

	else:
		form = MunicipioForm()

	return render_to_response('localidad/municipio.html',{'form':form},
		context_instance=RequestContext(request))