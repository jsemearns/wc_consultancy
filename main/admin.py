from django.contrib import admin

from main.models import (University, TotalStudents, Admission,
                         Requirement, Scholarship, Eligibility,
                         State, Tuition, Fee)

# Register your models here.
admin.site.register(University)
admin.site.register(TotalStudents)
admin.site.register(Admission)
admin.site.register(Requirement)
admin.site.register(Scholarship)
admin.site.register(Eligibility)
admin.site.register(State)
admin.site.register(Tuition)
admin.site.register(Fee)
