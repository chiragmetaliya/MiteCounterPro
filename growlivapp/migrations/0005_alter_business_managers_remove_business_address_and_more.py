# Generated by Django 5.0.3 on 2024-03-27 06:52

import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('growlivapp', '0004_video_delete_photo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='business',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='business',
            name='address',
        ),
        migrations.RemoveField(
            model_name='business',
            name='id',
        ),
        migrations.RemoveField(
            model_name='business',
            name='name',
        ),
        migrations.RemoveField(
            model_name='business',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='video',
            name='user',
        ),
        migrations.AddField(
            model_name='business',
            name='address_1',
            field=models.TextField(default='addr1', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='address_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='business_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='1234567890', max_length=128, region=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='business',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='growlivapp.business'),
        ),
        migrations.AlterField(
            model_name='business',
            name='contact_person_mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='business',
            name='contact_person_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='mite_videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['asf', 'avi', 'gif', 'm4v', 'mkv', 'mov', 'mp4', 'mpeg', 'mpg', 'ts', 'wmv', 'webm'])]),
        ),
    ]
