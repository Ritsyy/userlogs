# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-03 12:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0008_auto_20180303_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalitem',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalitem',
            name='user',
        ),
        migrations.RemoveField(
            model_name='historicalvariant',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalvariant',
            name='item',
        ),
        migrations.DeleteModel(
            name='HistoricalItem',
        ),
        migrations.DeleteModel(
            name='HistoricalVariant',
        ),
    ]
