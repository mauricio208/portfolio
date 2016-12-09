# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-12-09 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('first_meet_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='pacient',
            name='reports',
            field=models.ManyToManyField(to='toreports.Report'),
        ),
    ]
