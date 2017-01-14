from __future__ import unicode_literals

from django.db import models
from main.models.state import State

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=255)
    background = models.TextField(blank=True, null=True)
    state = models.ForeignKey(State)
    acceptance_rate = models.FloatField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class TotalStudents(models.Model):
    total_number = models.IntegerField()
    year = models.CharField(max_length=4)
    university = models.ForeignKey(University, related_name='total_students')
    is_international = models.BooleanField(default=False)
