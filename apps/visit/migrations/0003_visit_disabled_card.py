# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-10 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0002_auto_20180109_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='disabled_card',
            field=models.CharField(default='', max_length=20, verbose_name='残疾证号'),
        ),
    ]
