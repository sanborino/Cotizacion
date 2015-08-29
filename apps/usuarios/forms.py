from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
    	super(UserForm, self).__init__(*args, **kwargs)
    	self.fields['username'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['first_name'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['last_name'].widget.attrs.update({'class' : 'form-control'})
    	self.fields['email'].widget.attrs.update({'class' : 'form-control'})