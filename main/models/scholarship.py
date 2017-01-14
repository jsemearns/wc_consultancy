from __future__ import unicode_literals

from django.db import models

from main.models.university import University


class Scholarship(models.Model):
    detail = models.TextField(blank=True, null=True)
    additional_detail = models.TextField(blank=True, null=True)
    university = models.ForeignKey(University, related_name='scholarship')


class Eligibility(models.Model):
    """
    This model is used for each eligibility item specified when applying
    for a scholarship
    """
    detail = models.TextField(blank=True, null=True)
    scholarship = models.ForeignKey(Scholarship, related_name='eligibility')
