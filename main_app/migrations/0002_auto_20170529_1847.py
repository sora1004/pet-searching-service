# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-29 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='receiver2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='receiver2',
            field=models.IntegerField(null=True),
        ),
    ]