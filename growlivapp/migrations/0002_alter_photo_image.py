# Generated by Django 5.0.3 on 2024-03-15 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('growlivapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='C:\\Users\\abhis\\Desktop\\Education Docs\\Winter 2024\\Projects\\mite-counter\\mediamite_img/'),
        ),
    ]
