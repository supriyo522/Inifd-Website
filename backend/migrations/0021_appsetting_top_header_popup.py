# Generated by Django 4.0.4 on 2022-04-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_remove_enquiries_address_enquiries_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='appsetting',
            name='top_header_popup',
            field=models.BooleanField(default=False),
        ),
    ]