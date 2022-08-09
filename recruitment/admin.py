from django.contrib import admin
from .models import User, JobDescription, JobApplicant, Organization

admin.site.register(User)
admin.site.register(JobDescription)
admin.site.register(JobApplicant)
admin.site.register(Organization)

