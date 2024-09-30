# Generated by Django 5.0.3 on 2024-03-15 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feeder_mite_count', models.IntegerField(default=0)),
                ('predator_mite_count', models.IntegerField(default=0)),
                ('obj_detection_image', models.ImageField(upload_to='pred_mites')),
                ('scan_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]