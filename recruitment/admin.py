from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import JobApplication, JobDescription, JobApplication, Organization
from .forms import UserForm, CustomUserChangeForm, ApplicantForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active','first_name','last_name')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password','first_name','last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name','last_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class ApplicantAdmin(admin.ModelAdmin):
    form = ApplicantForm
    
admin.site.register(User, CustomUserAdmin)
admin.site.register(JobDescription)
admin.site.register(JobApplication)
admin.site.register(Organization)


