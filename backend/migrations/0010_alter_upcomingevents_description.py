# Generated by Django 4.0.4 on 2022-04-27 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_rename_event_date_upcomingevents_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevents',
            name='description',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]