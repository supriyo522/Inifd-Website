# Generated by Django 4.0.4 on 2022-04-30 09:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0031_pagegallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentors',
            name='profile',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
