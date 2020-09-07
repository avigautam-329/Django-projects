from django import forms


class TwitterForm(forms.Form):
    tweeterid = forms.CharField(max_length=30)
    
