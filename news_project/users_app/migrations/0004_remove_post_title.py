# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 14:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0003_auto_20160226_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]