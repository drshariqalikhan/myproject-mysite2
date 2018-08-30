# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-11 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myop_app', '0006_journeydata_is_onlinepreopelig'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journeydata',
            name='satisfaction_score',
        ),
        migrations.AddField(
            model_name='journeydata',
            name='is_OpCancelled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='is_PatientNoShow',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='is_PostOpComplication',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='is_PostOpDvt',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='is_PostOpInpatient',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='is_PostOpLrti',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='is_PostOpReadmission',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='is_PostOpSti',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='is_PostOpUti',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='pod15_satisfaction_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='journeydata',
            name='pod1_satisfaction_score',
            field=models.IntegerField(default=0),
        ),
    ]
