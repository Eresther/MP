# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20161010_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='processor',
            name='proc_qty',
            field=models.IntegerField(default=1),
        ),
    ]