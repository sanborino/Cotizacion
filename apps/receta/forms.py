from django import forms
from .models import Receta, Detalle, Ingrediente
# from django.forms.extras.widgets import SelectDateWidget
# from django.forms import widgets


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ('nombre','estado')

    def __init__(self, *args, **kwargs):
        super(RecetaForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['estado'].widget.attrs.update({'class': 'form-control'})

class DetalleForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = ('receta','item','cantidad','valor','estado')
        
    def __init__(self, *args, **kwargs):
    	super(DetalleForm, self).__init__(*args, **kwargs)
        self.fields['receta'].queryset = Receta.objects.filter(estado=1)
        self.fields['item'].queryset = Ingrediente.objects.order_by('nombre')
    	self.fields['cantidad'].widget.attrs.update({'class': 'form-control'})
        self.fields['valor'].widget.attrs.update({'class': 'form-control', 'readonly': True})
        self.fields['estado'].widget.attrs.update({'class': 'form-control', 'checked': True, 'readonly': True})

        for field in self.fields.itervalues():
            field.widget.attrs.update({'class': 'form-control'})
    	
class EditReceta(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ('costo','venta','nombre', 'estado',)

    def __init__(self, *args, **kwargs):
        super(EditReceta, self).__init__(*args, **kwargs)
        self.fields['costo'].widget.attrs.update({'class': 'form-control', 'readonly': True})
        self.fields['venta'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update({'class': 'form-control', 'readonly': True})
        self.fields['estado'].widget.attrs.update({'class': 'form-control'})


# class DetalleForm(forms.Form):

#     cantidad = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
#     valor = forms.DecimalField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
#     item = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices='')
#     receta = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices='')