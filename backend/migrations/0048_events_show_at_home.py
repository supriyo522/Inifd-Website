# Generated by Django 4.0.4 on 2022-05-05 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0047_placementpartners_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='show_at_home',
            field=models.BooleanField(default=False),
        ),
    ]
