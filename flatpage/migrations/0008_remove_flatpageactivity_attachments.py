# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-09 20:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpage', '0007_auto_20161207_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flatpageactivity',
            name='attachments',
        ),
    ]
