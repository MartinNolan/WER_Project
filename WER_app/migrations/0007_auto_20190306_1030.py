# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-06 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WER_app', '0006_page_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='picture',
            field=models.ImageField(blank=True, height_field=200, null=True, upload_to='', width_field=200),
        ),
    ]