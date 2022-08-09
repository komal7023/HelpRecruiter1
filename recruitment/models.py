from random import choices
from secrets import choice
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    contact_number = models.CharField(max_length=12)
    organization = models.CharField(max_length=100, blank=True, default='') 

    def __str__(self):
        return self.first_name 

class Organization(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=40)
    country = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=12)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name 

 
class JobDescription(models.Model):
    JOB_CAT_CHOICES =(
        ('HR','HR'),
        ( 'Frontend','Frontend'), 
        ('Backend', 'Backend'),
        ('Full stack','Full stack'), 
        ('Dev Ops','Dev Ops'), 
        ('BDE','BDE') ,
        ('others','others'),
    )

    EMLOYMENT_CHOICES = (
        ('Part time','Part-time'),
        ('Full time','Full-time'),
    )

    job_category = models.CharField(max_length=30, choices=JOB_CAT_CHOICES)
    job_title = models.CharField(max_length=30)
    job_location = models.CharField(max_length=30)
    employment_type = models.CharField(max_length=30, choices=EMLOYMENT_CHOICES)
    organizaton = models.CharField(max_length=40)
    mandatory_qualification = models.CharField(max_length=40)
    optional_qualification = models.CharField(max_length=40)
    experience = models.IntegerField()
    what_is_expected = models.CharField(max_length=10)
    what_we_offer = models.CharField(max_length=10)

    def __str__(self):
        return self.job_title 

    class Meta:
        permissions = (
            ('read_item','Can read item'),
        )

class JobApplicant(models.Model):
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('in_progress','In_progress'),
        ('selected', 'Selected'),
        ('rejected','Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_description = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    resume = models.FileField()
    notice_period = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.user