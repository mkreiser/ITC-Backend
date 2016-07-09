# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_event_relay_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='relay_members',
        ),
        migrations.RemoveField(
            model_name='result',
            name='athlete',
        ),
        migrations.AddField(
            model_name='result',
            name='athlete',
            field=models.ManyToManyField(to='app.Athlete'),
        ),
    ]