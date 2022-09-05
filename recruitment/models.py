import pdb
from random import choices
from secrets import choice
from typing_extensions import Required
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


        
class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
        
 

class Organization(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40)
    country = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=12)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name 

 
class JobDescription(models.Model):
   
    class JobCategories(models.TextChoices):
        hr= 'hr',_('HR')
        frontend='frontend',_('Frontend'), 
        backend= 'backend',_('Backend'),
        fullstack='fullstack',_('Fullstack'), 
        devops='devops',_('DevOps'), 
        bde='bde',_('BDE') ,
        others='others',_('Others')
    
    class EmployementTypes(models.TextChoices):
        part_time='part_time',_('Part-time'),
        full_time='full_time',_('Full-time')

    job_brief = models.TextField(blank=True)
    responsibilities = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    job_category = models.CharField(max_length=30, choices=JobCategories.choices)
    job_title = models.TextField()
    job_location = models.CharField(max_length=30)
    employment_type = models.CharField(max_length=30, choices=EmployementTypes.choices)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    mandatory_qualification = models.CharField(max_length=40)
    optional_qualification = models.CharField(max_length=40)
    experience = models.IntegerField(default=0)
    

    def __str__(self):
        return self.job_title 

    class Meta:
        permissions = (
            ('read_item','Can read item'),
        )

class JobApplication(models.Model):
    
    class StatusType(models.TextChoices):
        pending='pending',_('Pending'),
        in_progress='in_progress',_('In progress'),
        selected='selected',_('Selected'),
        rejected='rejected',_('Rejected'),

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_description = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    resume = models.FileField(upload_to=None) 
    notice_period = models.IntegerField()
    status = models.CharField(max_length=20, choices=StatusType.choices, default=StatusType.pending)

