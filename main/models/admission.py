from __future__ import unicode_literals

from django.db import models

from main.models.university import University

PROGRAM_TYPE = (
    (0, 'Undergraduate'),
    (1, 'Graduate')
)

ADMISSION_TYPE = (
    (0, 'Freshman'),
    (1, 'Transfer')
)

class Admission(models.Model):
    program_type = models.IntegerField(default=0, choices=PROGRAM_TYPE)
    admission_type = models.IntegerField(default=0, choices=ADMISSION_TYPE)
    detail = models.TextField(blank=True, null=True)
    university = models.ForeignKey(University, related_name='admission')

    def __unicode__(self):
        return '{}:{} {}'.format(self.university.name,
                                 PROGRAM_TYPE[self.program_type][1],
                                 ADMISSION_TYPE[self.admission_type]
                                                [1])


class Requirement(models.Model):
    detail = models.TextField()
    admission = models.ForeignKey(Admission, related_name='requirements')

    def __unicode__(self):
        return '{}:{} {}'.format(self.admission.university.name,
                                PROGRAM_TYPE[self.admission.program_type][1],
                                ADMISSION_TYPE[self.admission.admission_type]
                                                [1])
