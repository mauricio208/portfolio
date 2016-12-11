from __future__ import unicode_literals

from django.db import models

class Report(models.Model):
    date=models.DateField(blank=True, null=True)
    text=models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        from datetime import datetime as dt
        if self.date:
            self.date=dt.strptime(self.date,'%d/%m/%Y').date()
        super(Report, self).save(*args, **kwargs)
        

class Pacient(models.Model):
    name=models.CharField(max_length=255)
    first_meet_on=models.DateTimeField(blank=True, null=True)
    reports=models.ManyToManyField(Report)
