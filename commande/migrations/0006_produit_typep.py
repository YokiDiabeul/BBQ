# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0005_auto_20170927_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='typeP',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
