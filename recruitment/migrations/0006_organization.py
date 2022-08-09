# Generated by Django 4.1 on 2022-08-09 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0005_user_organization'),
    ]

    operations = [
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
    ]
