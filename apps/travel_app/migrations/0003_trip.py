# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-27 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0002_auto_20171227_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('travelfrom', models.DateTimeField(auto_now_add=True)),
                ('travelto', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('my_trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planner', to='travel_app.User')),
                ('travellers', models.ManyToManyField(related_name='joiner', to='travel_app.User')),
            ],
        ),
    ]
