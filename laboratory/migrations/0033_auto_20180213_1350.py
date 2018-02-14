# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-13 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0032_auto_20180213_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationstruture',
            name='father',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='laboratory.OrganizationStruture'),
        ),
        migrations.AlterField(
            model_name='organizationstruture',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='laboratory.OrganizationGroup'),
        ),
    ]
