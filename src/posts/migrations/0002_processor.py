# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proc_model', models.CharField(max_length=100)),
                ('proc_socket', models.IntegerField()),
                ('proc_watts', models.IntegerField()),
                ('proc_content', models.TextField()),
            ],
        ),
    ]
