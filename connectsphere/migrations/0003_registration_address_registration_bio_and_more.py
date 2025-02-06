# Generated by Django 5.1.4 on 2025-01-31 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connectsphere', '0002_post_comment_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
