# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 13:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0003_auto_20170927_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commandetotal',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
