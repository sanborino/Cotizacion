# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .forms import UserForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy

def editar_perfil(request):

    if request.method == 'POST':
        # formulario enviado
        user_form = UserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            # formulario validado correctamente
            user_form.save()
            return HttpResponseRedirect('/actualizado/')

    else:
        # formulario inicial
        user_form = UserForm(instance=request.user)

    return render_to_response('usuarios/perfil.html', { 'user_form': user_form }, 
        context_instance=RequestContext(request))

class perfil(TemplateView):
    template_name = 'usuarios/perfil_actualizado.html'
    success_url = reverse_lazy('perfil')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(perfil, self).dispatch(*args, **kwargs)