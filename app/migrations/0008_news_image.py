# Generated by Django 4.0.5 on 2022-06-21 09:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]
