# Generated by Django 4.0.4 on 2022-05-05 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0049_mediacoverage_show_at_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='academictours',
            name='show_at_home',
            field=models.BooleanField(default=False),
        ),
    ]
