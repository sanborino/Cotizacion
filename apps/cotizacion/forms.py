from django import forms
from .models import Cotizacion

class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ('empresa','cliente','receta','personas','venta', 'extra','descripcion',
            'total','fechaFinal','estado')

    def __init__(self, *args, **kwargs):
    	super(CotizacionForm, self).__init__(*args, **kwargs)
    	self.fields['empresa'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['cliente'].widget.attrs.update({'class' : 'form-control'})
        self.fields['receta'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['personas'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['venta'].widget.attrs.update({'class' : 'form-control', 'readonly': True})
        self.fields['extra'].widget.attrs.update({'class' : 'form-control'})
        self.fields['descripcion'].widget.attrs.update({'class' : 'form-control'})
        self.fields['total'].widget.attrs.update({'class' : 'form-control', 'readonly': True})
        self.fields['fechaFinal'].widget.attrs.update({'class' : 'form-control', 'placeholder': 'AAAA-MM-DD'})
        self.fields['estado'].widget.attrs.update({'class' : 'form-control', 'value': 'Pendiente', 'readonly': True})

        for field in self.fields.itervalues():
            field.widget.attrs.update({'class': 'form-control'})

class AprobacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ('estado',)

    def __init__(self, *args, **kwargs):
        super(AprobacionForm, self).__init__(*args, **kwargs)
        self.fields['estado'].widget.attrs.update({'class' : 'form-control'})   


class InformalForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ('empresa','cliente','receta','descripcion', 'fechaFinal','estado')

    def __init__(self, *args, **kwargs):
        super(InformalForm, self).__init__(*args, **kwargs)
        self.fields['empresa'].widget.attrs.update({'class' : 'form-control'})
        self.fields['cliente'].widget.attrs.update({'class' : 'form-control'})
        self.fields['receta'].widget.attrs.update({'class' : 'form-control'})
        self.fields['descripcion'].widget.attrs.update({'class' : 'form-control'})
        self.fields['fechaFinal'].widget.attrs.update({'class' : 'form-control', 'placeholder': 'AAAA-MM-DD'})
        self.fields['estado'].widget.attrs.update({'class' : 'form-control', 'value': 'Pendiente', 'readonly': True})


