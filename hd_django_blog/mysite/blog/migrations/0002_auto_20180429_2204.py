# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-29 22:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 29, 22, 4, 3, 542817, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 29, 22, 4, 3, 542173, tzinfo=utc)),
        ),
    ]
