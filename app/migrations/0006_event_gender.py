# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_modelenums'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='gender',
            field=models.CharField(choices=[('Both', 'Both'), ('Male', 'Male'), ('Female', 'Female')], default='Both', max_length=10),
        ),
    ]