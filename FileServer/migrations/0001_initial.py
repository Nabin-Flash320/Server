# Generated by Django 4.1 on 2022-10-15 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=300, unique=True)),
                ('path', models.CharField(max_length=300, null=True, unique=True)),
                ('slug', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=300)),
                ('file_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FileServer.filetype')),
            ],
        ),
    ]
