# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-06 11:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WER_app', '0008_auto_20190306_1039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='closingH',
            new_name='openingHours',
        ),
        migrations.RemoveField(
            model_name='page',
            name='openingH',
        ),
    ]