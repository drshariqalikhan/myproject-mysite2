# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-12 09:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myop_app', '0013_auto_20180812_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journeydata',
            name='days_to_op',
        ),
        migrations.RemoveField(
            model_name='journeydata',
            name='is_OnlinePreopElig',
        ),
    ]