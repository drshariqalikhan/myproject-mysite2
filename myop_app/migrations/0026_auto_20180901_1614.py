# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-01 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myop_app', '0025_auto_20180901_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journeydata',
            name='date_of_birth',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
