# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-03 22:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20170531_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.Report_type'),
        ),
    ]
