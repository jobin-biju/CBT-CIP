# Generated by Django 5.1.4 on 2025-02-03 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connectsphere', '0006_registration_profilepic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='profilepic',
        ),
        migrations.AddField(
            model_name='registration',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
