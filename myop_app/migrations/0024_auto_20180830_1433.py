# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-30 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myop_app', '0023_journeydata_patient_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journeydata',
            name='journey_point',
            field=models.CharField(blank=True, default='preop_incomplete', max_length=100),
        ),
    ]
