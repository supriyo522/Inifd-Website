# Generated by Django 4.0.4 on 2022-04-27 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_alter_upcomingevents_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastevents',
            name='description',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]