# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_processor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moth_model', models.CharField(max_length=100)),
                ('moth_watts', models.IntegerField()),
                ('moth_content', models.TextField()),
                ('moth_image', models.FileField(blank=True, null=True, upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='processor',
            name='proc_image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='moth_socket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Processor'),
        ),
    ]