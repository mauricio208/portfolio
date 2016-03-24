from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProjectsModel(models.Model):
    """
    Description: Principal model of the projects app. It represent the object with all the relation of a project
    """
    name=models.CharField(max_length=250, unique=True, null=False, blank=False)
    description = models.TextField(nique=True,null=False, blank=False)
    technologies= models.ManyToManyField('TechnologiesModel', null=True,blank=True)
    media= models.ManyToManyField('MediaModel', null=False, blank=False)

class MediaModel(models.Model):
    """
    Description: Model that holds all media information of the project
    """
	media_link = models.TextField(null=False, blank=False)
	description = models.TextField(null=True, blank=True)
	snippet = models.TextField(null=True, blank=True)

class TechnologiesModel(models.Model):
    """
    Description: list all possible technologies
    """
    name = models.CharField(unique=True, null=False, blank=False, max_length=50)

	
