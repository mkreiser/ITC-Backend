# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 02:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('membership', models.CharField(choices=[('Club', 'Club'), ('Alum', 'Alum'), ('Elite', 'Elite')], default='Club', max_length=10)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distanceEvent', models.BooleanField(default=False)),
                ('gender', models.CharField(choices=[('Both', 'Both'), ('Male', 'Male'), ('Female', 'Female')], default='Both', max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('relay', models.BooleanField(default=False)),
                ('season', models.CharField(choices=[('XC', 'XC'), ('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('host', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True)),
                ('resultURL', models.TextField(blank=True)),
                ('season', models.CharField(choices=[('XC', 'XC'), ('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')], max_length=10)),
                ('splitURL', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModelEnums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distanceResult', models.BooleanField(default=False)),
                ('performance', models.FloatField()),
                ('result_membership', models.CharField(choices=[('Club', 'Club'), ('Alum', 'Alum'), ('Elite', 'Elite')], default='Club', max_length=6)),
                ('athlete', models.ManyToManyField(to='app.Athlete')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Event')),
                ('meet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Meet')),
            ],
        ),
    ]
