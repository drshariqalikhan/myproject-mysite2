# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-01 08:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myop_app', '0024_auto_20180830_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='journeydata',
            name='IsActiveSession',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='age_at_op',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.date(2018, 9, 1)),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='dbp_at_op',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='gender',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='heartrate_at_op',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='height',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='patient_firstname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='patient_lastname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='patient_mobile_number',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='planned_postop_location',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='race',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='sbp_at_op',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='weight_at_op',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]