# Generated by Django 4.0.4 on 2022-04-27 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_rename_date_upcomingevents_event_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upcomingevents',
            old_name='event_date',
            new_name='date',
        ),
    ]
