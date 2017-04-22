# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-22 05:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.TextField(blank=True, null=True)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('ts_created', models.DateTimeField(auto_now=True)),
                ('ts_updated', models.DateTimeField(auto_now=True, null=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
                ('profile_image', models.ImageField(upload_to='profile_images/')),
                ('about', models.TextField()),
                ('education', models.TextField()),
                ('contact_info', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]