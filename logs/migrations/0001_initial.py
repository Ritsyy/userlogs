# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-19 19:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('product_code', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, choices=[(None, 'Please Select'), ('S', 'SMALL'), ('M', 'MEDIUM'), ('L', 'LARGE'), ('XL', 'EXTRA LARGE')], default=None, max_length=3, null=True)),
                ('cloth', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('selling_price', models.IntegerField()),
                ('cost_price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logs.Item')),
                ('properties', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='logs.Property')),
            ],
        ),
    ]
