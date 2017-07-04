# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
                ('age', models.IntegerField(verbose_name=16)),
            ],
        ),
        migrations.CreateModel(
            name='Wing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('age', models.IntegerField(verbose_name=16)),
                ('favourite', models.CharField(max_length=64)),
                ('skill', models.CharField(max_length=128)),
            ],
        ),
    ]
