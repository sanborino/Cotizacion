# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from forms import RecetaForm, DetalleForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from apps.ingrediente.models import Ingrediente
from .models import Detalle, Receta
from django.db.models import Sum
from .forms import EditReceta
from django.http import HttpResponse


@login_required
def RegistrarReceta(request):
	if not request.user.is_staff:
		return HttpResponse("<h1>Acceso restringido consulte al administrador</h1>")

	if request.method == 'POST':
		form = RecetaForm(request.POST)
		if form.is_valid():

			form.save()

			return HttpResponseRedirect('/administracion/ingredientes/')

	else:
		form = RecetaForm()

	return render_to_response('administracion/receta.html',{'form':form},
		context_instance=RequestContext(request))

@login_required
def ingredientes(request):
	if not request.user.is_staff:
		return HttpResponse("<h1>Acceso restringido consulte al administrador</h1>")
	# suma = Ingrediente.objects.aggregate(Avg('costo')) este es para promediar
	# suma = Ingrediente.objects.aggregate(Sum('costo')) este es para sumar
	# suma = Ingrediente.objects.count()
	# receta = Receta.objects.latest()
	items = Detalle.objects.filter(estado=1)
	articulo = Ingrediente.objects.all()
	if request.method == 'POST':
		form = DetalleForm(request.POST)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/administracion/ingredientes/')

	else:
		form = DetalleForm()
		
	ctx = {'form':form,'articulos':articulo, 'items':items}
	return render_to_response('administracion/ingredientes.html',ctx,
		context_instance=RequestContext(request))

@login_required
def editar(request):
	
	if not request.user.is_staff:
		return HttpResponse("<h1>Acceso restringido consulte al administrador</h1>")
	items = Detalle.objects.filter(estado=1)
	nombre = Receta.objects.get(estado=1)
	if request.method == 'POST':
		Receta_form = EditReceta(request.POST,instance=nombre)
	
		if Receta_form.is_valid():
			Receta_form.save()

			return HttpResponseRedirect('/localidad/confirma/')

	else:
		Receta_form = EditReceta(instance=nombre)
		
	ctx = {'Receta_form': Receta_form,'items': items}
	return render_to_response('administracion/confirmar.html',ctx,
		context_instance=RequestContext(request))

@login_required
def catalogoRecetas(request):
	if not request.user.is_staff:
		return HttpResponse("<h1>Acceso restringido consulte al administrador</h1>")

	articulo = Receta.objects.all()

	ctx = {'articulo':articulo}
	return render_to_response('administracion/catalogoR.html',ctx,context_instance=RequestContext(request))
