# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-26 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sest', '0008_field_field_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
