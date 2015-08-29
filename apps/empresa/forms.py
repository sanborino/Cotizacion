from django import forms
from .models import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('nombre','direccion','telefono','celular','correo',
        	'contacto','municipio')

    def __init__(self, *args, **kwargs):
    	super(EmpresaForm, self).__init__(*args, **kwargs)
    	self.fields['nombre'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['direccion'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['telefono'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['celular'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['correo'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['contacto'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['municipio'].widget.attrs.update({'class' : 'form-control'})
    	