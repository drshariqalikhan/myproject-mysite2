# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-12 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myop_app', '0011_auto_20180812_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journeydata',
            name='days_to_op',
            field=models.IntegerField(blank=True),
        ),
    ]