# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-15 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0028_auto_20180214_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinventory',
            name='cas_id_number',
            field=models.TextField(verbose_name='CAS ID number'),
        ),
        migrations.AlterField(
            model_name='clinventory',
            name='name',
            field=models.TextField(verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='clinventory',
            name='url',
            field=models.TextField(verbose_name='URL'),
        ),
    ]
