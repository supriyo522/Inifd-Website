# Generated by Django 4.0.4 on 2022-04-29 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_alter_enquirystatus_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiries',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
