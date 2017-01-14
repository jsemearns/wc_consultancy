from django.shortcuts import render
from django.views.generic import TemplateView

from main.models import University


class UniversityTemplateView(TemplateView):
    template_name = 'universities/university.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UniversityTemplateView, self).get_context_data(
                        *args, **kwargs)
        context['universities'] = University.objects.all().order_by('name')
        return context
