# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-17 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0012_auto_20170816_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='author_response',
            field=models.TextField(blank=True, null=True),
        ),
    ]
