# Generated by Django 5.0.3 on 2024-04-01 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('growlivapp', '0009_alter_video_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='address_1',
        ),
        migrations.RemoveField(
            model_name='business',
            name='address_2',
        ),
        migrations.RemoveField(
            model_name='business',
            name='contact_person_mobile',
        ),
    ]
