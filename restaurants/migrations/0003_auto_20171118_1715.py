# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 17:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20171118_1611'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['-is_open']},
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='location',
        ),
    ]