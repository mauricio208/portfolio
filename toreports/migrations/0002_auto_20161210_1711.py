# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-12-10 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toreports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
