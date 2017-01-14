from __future__ import unicode_literals

from django.db import models

from main.models.university import University


class Tuition(models.Model):
    detail = models.TextField(blank=True, null=True)
    additional_detail = models.TextField(blank=True, null=True)
    university = models.ForeignKey(University, related_name='tuition')


class Fee(models.Model):
    """
    This model is used for each fee item specified on each
    university
    """
    name = models.CharField(max_length=255)
    amount = models.FloatField()
    detail = models.TextField(blank=True, null=True)
    tuition = models.ForeignKey(Tuition, related_name='fee')
