# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-02 18:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WER_app', '0003_auto_20190302_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='atmostphere',
            new_name='atmosphere',
        ),
    ]