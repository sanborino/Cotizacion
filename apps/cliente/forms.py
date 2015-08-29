from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre','telefono','celular','correo', 'evento')

    def __init__(self, *args, **kwargs):
    	super(ClienteForm, self).__init__(*args, **kwargs)
    	self.fields['nombre'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['telefono'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['celular'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['correo'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['evento'].widget.attrs.update({'class' : 'form-control'})

class Clientes(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre','telefono','celular','correo','alta','evento',)

    def __init__(self, *args, **kwargs):
        super(Clientes, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class' : 'form-control'})
        self.fields['telefono'].widget.attrs.update({'class' : 'form-control'})
        self.fields['celular'].widget.attrs.update({'class' : 'form-control'})
        self.fields['correo'].widget.attrs.update({'class' : 'form-control'})
        self.fields['alta'].widget.attrs.update({'class' : 'form-control'})
        self.fields['evento'].widget.attrs.update({'class' : 'form-control'})
    	