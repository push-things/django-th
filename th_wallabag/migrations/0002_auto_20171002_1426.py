# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 12:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('th_wallabag', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallabag',
            name='trigger',
        ),
        migrations.DeleteModel(
            name='Wallabag',
        ),
    ]