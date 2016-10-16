# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_submit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=120)),
                ('cost', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Case')),
                ('gpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.GPU')),
                ('mem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Memory')),
                ('mobo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Motherboard')),
                ('proc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Processor')),
                ('psu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.PSU')),
                ('stor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Storage')),
            ],
        ),
        migrations.RemoveField(
            model_name='submit',
            name='proc',
        ),
        migrations.DeleteModel(
            name='Submit',
        ),
    ]