# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-09 07:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='path',
            field=models.ImageField(upload_to='visit', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Area', verbose_name='所属地区'),
        ),
    ]
