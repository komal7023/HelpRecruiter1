from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm   



class AuthenticationFormWithInactiveUsersOkay(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass


class UserForm (UserCreationForm): 
    username = forms.CharField(label = "Username")
    class Meta:
        model = User
        fields = ('email','username')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ( "email",)        


class AppForm(forms.ModelForm):
    contact_number = forms.CharField(max_length=12)
    # resume = forms.FileField()
    notice_period = forms.IntegerField()
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError('This email address is already in use.')    
    
    