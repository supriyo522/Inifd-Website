# Generated by Django 4.0.4 on 2022-05-01 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0045_testimonials_created_by_testimonials_show_at_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='placements',
            name='show_at_home',
            field=models.BooleanField(default=False),
        ),
    ]
