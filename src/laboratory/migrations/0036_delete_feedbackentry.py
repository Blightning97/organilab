# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 07:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0035_auto_20180621_0020'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FeedbackEntry',
        ),
    ]