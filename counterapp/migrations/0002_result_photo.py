# Generated by Django 5.0.3 on 2024-03-15 07:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counterapp', '0001_initial'),
        ('growlivapp', '0003_alter_business_options_alter_photo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='photo',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='growlivapp.photo'),
            preserve_default=False,
        ),
    ]
