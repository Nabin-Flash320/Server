# Generated by Django 4.1 on 2022-10-25 12:46

import FileServer.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FileServer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='file_name',
        ),
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default='', upload_to=FileServer.models.upload_file_to),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_type',
            field=models.CharField(choices=[('txt', 'txt'), ('bin', 'bin')], max_length=10),
        ),
        migrations.DeleteModel(
            name='FileType',
        ),
    ]
