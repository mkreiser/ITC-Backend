# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160705_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelEnums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
