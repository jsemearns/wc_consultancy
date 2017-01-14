from __future__ import unicode_literals

from django.db import models

from main.models.university import University


class Admission(models.Model):
    detail = models.TextField(blank=True, null=True)
    additional_detail = models.TextField(blank=True, null=True)
    university = models.ForeignKey(University, related_name='admission')


class Requirement(models.Model):
    detail = models.TextField()
    admission = models.ForeignKey(Admission, related_name='requirement')
