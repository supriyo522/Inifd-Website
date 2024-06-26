# Generated by Django 4.0.4 on 2022-05-01 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0041_academictours_created_by_awards_created_by_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='careted_by',
            new_name='created_by',
        ),
        migrations.AddField(
            model_name='gallery',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='globalopportunities',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
