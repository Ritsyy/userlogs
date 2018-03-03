# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-03 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0007_historicalvariant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalitem',
            name='variant',
        ),
        migrations.RemoveField(
            model_name='item',
            name='variant',
        ),
        migrations.AddField(
            model_name='historicalvariant',
            name='item',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='logs.Item'),
        ),
        migrations.AddField(
            model_name='variant',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='logs.Item'),
        ),
    ]
