# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from forms import EmpresaForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


@login_required
def RegistrarEmpresa(request):
	if not request.user.is_staff:
		return HttpResponse("<h1>Acceso restringido consulte al administrador</h1>")

	if request.method == 'POST':
		form = EmpresaForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/localidad/confirma/')

	else:
		form = EmpresaForm()

	return render_to_response('localidad/empresa.html',{'form':form},
		context_instance=RequestContext(request))