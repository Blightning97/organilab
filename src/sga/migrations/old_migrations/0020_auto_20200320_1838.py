# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-21 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sga', '0019_auto_20200118_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warningclass',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='warningclass',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='warningclass',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
    ]
