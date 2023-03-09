# Generated by Django 4.0.4 on 2022-05-01 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0046_placements_show_at_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='placementpartners',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='placementpartners',
            name='show_at_home',
            field=models.BooleanField(default=False),
        ),
    ]