from django import forms
from .models import User_form_model

class User_form(forms.ModelForm):
    class Meta:
        model = User_form_model
        fields = ['name', 'email','occupation', 'message']