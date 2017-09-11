# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-30 21:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_auto_20170529_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('length', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('sex', models.CharField(blank=True, max_length=20, null=True)),
                ('predominant_color', models.CharField(blank=True, max_length=50, null=True)),
                ('height', models.CharField(blank=True, max_length=20, null=True)),
                ('weight', models.CharField(blank=True, max_length=20, null=True)),
                ('age', models.CharField(blank=True, max_length=20, null=True)),
                ('ident_mark_feat', models.CharField(blank=True, max_length=300, null=True)),
                ('collar', models.CharField(blank=True, max_length=100, null=True)),
                ('coat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.Coat')),
            ],
        ),
        migrations.CreateModel(
            name='Pet_breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pet_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ident_det', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.Address')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Pet')),
            ],
        ),
        migrations.CreateModel(
            name='Report_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.Report_type'),
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pet_breed',
            name='pet_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Pet_type'),
        ),
        migrations.AddField(
            model_name='pet',
            name='pet_breed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.Pet_breed'),
        ),
        migrations.AddField(
            model_name='pet',
            name='pet_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.Pet_type'),
        ),
    ]
