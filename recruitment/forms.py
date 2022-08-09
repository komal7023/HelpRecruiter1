from django import forms
from .models import User

class UserForm(forms.ModelForm):
    resume = forms.FileField()
    notice_period = forms.IntegerField()

    class Meta:
        model = User
        fields="__all__" 
        
