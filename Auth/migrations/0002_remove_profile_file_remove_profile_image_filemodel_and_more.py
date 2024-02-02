# Generated by Django 5.0.1 on 2024-02-02 10:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='file',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='file')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file', to='Auth.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
