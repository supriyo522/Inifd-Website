# Generated by Django 4.0.4 on 2023-02-24 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0057_fashionshows_interiorexhibition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
