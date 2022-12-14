from django import forms
from .models import JobApplication, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm   


class AuthenticationFormWithInactiveUsersOkay(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass

class UserForm (UserCreationForm): 
    username = forms.CharField(label = "Username")
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ( "email",)        
  
    
class ApplicantForm(forms.ModelForm):
    def __init__(self, **kwargs):

        self.base_fields['user'].initial = kwargs.pop('user', None)
        self.base_fields['job_description'].initial = kwargs.pop('job_description', None)

        super(ApplicantForm, self).__init__(**kwargs)
        print(self.fields)
 
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20) 
    resume = forms.FileField() 
      
    class Meta:
        model = JobApplication
        widgets = {
            "user": forms.HiddenInput(),
            "job_description": forms.HiddenInput(),
            "status": forms.HiddenInput(),
        }
        fields = "__all__" 
   
    def save(self, commit=True, *args, **kwargs):
        m = super(ApplicantForm, self).save(commit=False, *args, **kwargs)
        if commit:
            m.save()
        return m    

   