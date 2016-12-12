# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-07 01:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flatpage', '0003_remove_flatpageactivity_attachments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpageactivity',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flatpages', to='core.ActivityCollection'),
        ),
    ]
