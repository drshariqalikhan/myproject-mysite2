# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-20 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myop_app', '0019_auto_20180820_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journeydata',
            name='UnixTimeOfLastSync',
            field=models.CharField(blank=True, default='1', max_length=100),
        ),
    ]