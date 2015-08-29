from django import forms
from .models import Evento


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
    	super(EventoForm, self).__init__(*args, **kwargs)
    	self.fields['nombre'].widget.attrs.update({'class' : 'form-control',
    	 'placeholder' : 'Nombre del evento'})
