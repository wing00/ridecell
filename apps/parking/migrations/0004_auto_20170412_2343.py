# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 23:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0003_auto_20170412_2217'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Locations',
            new_name='Location',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='location',
            new_name='point',
        ),
    ]
