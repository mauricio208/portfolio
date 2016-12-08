from __future__ import unicode_literals

from django.db import models

class Report(models.Model):
    date=models.DateTimeField(blank=True, null=True)
    text=models.TextField(blank=True, null=True)

class Pacient(models.Model):
    name=models.CharField(max_length=255)
    first_meet_on=models.DateTimeField(blank=True, null=True)
    reports=models.ManyToManyField(Report)
