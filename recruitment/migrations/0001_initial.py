# Generated by Django 4.1 on 2022-09-02 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=40)),
                ('country', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JobDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_brief', models.TextField(blank=True)),
                ('responsibilities', models.TextField(blank=True)),
                ('skills', models.TextField(blank=True)),
                ('job_category', models.CharField(choices=[('hr', 'HR'), ('frontend', 'Frontend'), ('backend', 'Backend'), ('fullstack', 'Fullstack'), ('devops', 'DevOps'), ('bde', 'BDE'), ('others', 'Others')], max_length=30)),
                ('job_title', models.TextField()),
                ('job_location', models.CharField(max_length=30)),
                ('employment_type', models.CharField(choices=[('part_time', 'Part-time'), ('full_time', 'Full-time')], max_length=30)),
                ('mandatory_qualification', models.CharField(max_length=40)),
                ('optional_qualification', models.CharField(max_length=40)),
                ('experience', models.IntegerField(default=0)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.organization')),
            ],
            options={
                'permissions': (('read_item', 'Can read item'),),
            },
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to=None)),
                ('notice_period', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In progress'), ('selected', 'Selected'), ('rejected', 'Rejected')], max_length=20)),
                ('job_description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.jobdescription')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
