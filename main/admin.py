from django.contrib import admin

from main.models import (University, TotalStudents, Admission,
                         Requirement, Scholarship, Eligibility,
                         State, Tuition, Fee)

class UniversityAdmin(admin.ModelAdmin):
    search_fields = ['name', 'website']


# Register your models here.
admin.site.register(University, UniversityAdmin)
admin.site.register(TotalStudents)
admin.site.register(Admission)
admin.site.register(Requirement)
admin.site.register(Scholarship)
admin.site.register(Eligibility)
admin.site.register(State)
admin.site.register(Tuition)
admin.site.register(Fee)
