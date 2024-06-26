# Generated by Django 4.0.4 on 2022-05-01 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0038_alter_events_is_active_alter_events_is_upcoming'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='student_works')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='upcomingeventgallery',
            name='event',
        ),
        migrations.DeleteModel(
            name='PastEventGallery',
        ),
        migrations.DeleteModel(
            name='PastEvents',
        ),
        migrations.DeleteModel(
            name='UpcomingEventGallery',
        ),
        migrations.DeleteModel(
            name='UpcomingEvents',
        ),
    ]
