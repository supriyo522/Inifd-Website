# Generated by Django 4.0.4 on 2022-04-29 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0026_menuitems_delete_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitems',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]