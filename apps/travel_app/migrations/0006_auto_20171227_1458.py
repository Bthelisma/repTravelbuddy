# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-27 22:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0005_auto_20171227_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='travelfrom',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='travelto',
            new_name='start_date',
        ),
    ]