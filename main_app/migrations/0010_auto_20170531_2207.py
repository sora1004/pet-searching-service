# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-31 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20170531_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='pet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.Pet'),
        ),
    ]
