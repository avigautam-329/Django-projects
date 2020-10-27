import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30,render_value=False)))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True,max_length=30,render_value=False)))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. plz try another one."))
    
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("the two password fields did not match."))
            return self.cleaned_data
