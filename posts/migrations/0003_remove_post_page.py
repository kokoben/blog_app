# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-03 06:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20170226_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='page',
        ),
    ]
