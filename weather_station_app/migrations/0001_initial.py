# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-25 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('reg_time', models.DateTimeField(verbose_name='registration date and time')),
                ('entry_id', models.IntegerField(primary_key=True, serialize=False)),
                ('field1', models.FloatField(verbose_name='temperature')),
                ('field2', models.FloatField(verbose_name='humidity')),
            ],
        ),
    ]
