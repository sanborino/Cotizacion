# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from .forms import ClienteForm
from .models import Cliente
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


@login_required
def RegistrarCliente(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/localidad/confirma/')

	else:
		form = ClienteForm()

	return render_to_response('negocio/cliente.html',{'form':form},
		context_instance=RequestContext(request))

@login_required
def clientesTodos(request):

	clientes = Cliente.objects.all()

	ctx = {'clientes': clientes}
	return render_to_response('negocio/clientes.html',ctx,context_instance=RequestContext(request))

