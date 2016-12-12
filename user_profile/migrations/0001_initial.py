# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-02 21:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user_profile.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='', unique=True)),
                ('bio', models.TextField(blank=True, default='', verbose_name='About Me')),
                ('image', models.ImageField(blank=True, null=True, upload_to=user_profile.models.upload_location)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]