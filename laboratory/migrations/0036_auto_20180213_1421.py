# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-13 20:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0035_auto_20180213_1357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizationstruture',
            options={'verbose_name': 'Organization', 'verbose_name_plural': 'Organizations'},
        ),
        migrations.AlterField(
            model_name='organizationstruture',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group'),
        ),
        migrations.DeleteModel(
            name='OrganizationGroup',
        ),
    ]
