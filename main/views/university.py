from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from main.models import (University, Admission, Requirement)


class UniversityTemplateView(TemplateView):
    template_name = 'universities/university_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UniversityTemplateView, self).get_context_data(
                        *args, **kwargs)
        context['universities'] = University.objects.all().order_by('name')
        return context


class UniversityDetailTemplateView(TemplateView):
    template_name = 'universities/university_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UniversityDetailTemplateView, self).get_context_data(
                        *args, **kwargs)
        university = get_object_or_404(University, **kwargs)
        admissions = Admission.objects.filter(university=university)
        context['admissions'] = admissions
        context['university'] = university
        return context
