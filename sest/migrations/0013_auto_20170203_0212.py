# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-03 01:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sest', '0012_auto_20170203_0202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='field',
            old_name='value',
            new_name='_value',
        ),
    ]
