# Generated by Django 4.1 on 2022-09-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0004_alter_jobapplication_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='resume',
            field=models.FileField(upload_to='Documents/'),
        ),
    ]
