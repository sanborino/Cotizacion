from django import forms
from .models import Municipio


class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ('estado', 'nombre')

    def __init__(self, *args, **kwargs):
    	super(MunicipioForm, self).__init__(*args, **kwargs)
    	self.fields['estado'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['nombre'].widget.attrs.update({'class' : 'form-control',
    	 'placeholder' : 'Nombre del municipio'})
