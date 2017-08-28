from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class WebQuery(models.Model):
#    user = models.ForeignKey('auth.User')
    gene_name = models.CharField(max_length=200)
    #add local_name
    local_name = models.CharField(max_length=200)
    access_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.gene_name

class Gene(models.Model):
    key = models.AutoField
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Location (models.Model):
    key = models.AutoField
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Expression (models.Model):
    key = models.AutoField
    gene = models.ForeignKey(Gene)
    location = models.ForeignKey(Location)
    express = models.FloatField(null=True)

    def __str__(self):
        return self.gene + "+" + self.location
