from django import forms
from .models import JobApplication, JobDescription, User
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


class ApplicationForm(forms.ModelForm):
    contact_number = forms.CharField(max_length=12)
    resume = forms.FileField(required=False)
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
    
class ApplicantForm(forms.ModelForm):
    def __init__(self, **kwargs):
        # import pdb; pdb.set_trace()
        self.base_fields['user'].initial = kwargs.pop('user', None)
        # self.base_fields['job_description'] = kwargs.pop('job_description', None)
        super(ApplicantForm, self).__init__(**kwargs)

 
    resume = forms.FileField(required=False)    

    class Meta:
        model = JobApplication
        fields = "__all__"

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            JobApplication.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError('This email address is already in use.')    

class JobDescriptionForm(forms.ModelForm):
    class Meta:
        model = JobDescription
        fields = ('job_title','job_category','employment_type','organization')
