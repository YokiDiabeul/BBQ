# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0002_auto_20170927_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commandetotal',
            name='date',
            field=models.DateTimeField(verbose_name='Set date by Yoki'),
        ),
    ]
